import asyncio
import logging
import os

import yaml
from browser_use import Agent
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)

with open('config.yaml') as f:
    config = yaml.safe_load(f)


def load_documents():
    loader = DirectoryLoader(config['documents_dir'], glob="**/*.txt")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(docs)


def setup_rag():
    docs = load_documents()
    vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
    return vectorstore.as_retriever()


memory = ConversationBufferMemory()


def generate_response(query):
    retriever = setup_rag()
    relevant_docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    memory.save_context({"input": query}, {"output": ""})
    history = memory.load_memory_variables({})

    llm = ChatOpenAI(
        model=config['deepseek']['model'], api_key=config['deepseek']['api_key']
    )
    response = llm.invoke(
        f"Context: {context}\n\nHistory: {history}\n\nQuestion: {query}"
    )
    return f"{config['bot_disclaimer']}\n\n{response.content}"


async def process_messages():
    agent = Agent(
        llm=ChatOpenAI(model="gpt-4o"),
        task="Log in to LinkedIn, go to messages, check for new messages, and reply based on the provided knowledge base.",
    )
    while True:
        try:
            result = await agent.run()
            logging.info(f"Agent result: {result}")
            time.sleep(60)
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            time.sleep(300)


if __name__ == "__main__":
    logging.info("Starting bot...")
    asyncio.run(process_messages())
