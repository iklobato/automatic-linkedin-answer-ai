# **Automatic LinkedIn Answer AI**

Automatically respond to LinkedIn messages from recruiters using AI. This bot leverages your resume and professional documents to generate precise, context-aware answers. It uses browser automation, Retrieval-Augmented Generation (RAG), and memory to ensure accurate and personalized responses.

---

## **Features**
- **Automated LinkedIn Messaging**: Replies to recruiter messages in real-time.
- **Document-Based Answers**: Uses your resume and professional documents to generate responses.
- **Precision with RAG**: Retrieves relevant information from your documents for accurate answers.
- **Memory for Context**: Remembers previous interactions for consistent responses.
- **Easy Setup**: Simple configuration and no need for LinkedIn API credentials.

---

## **Use Cases**
1. **Job Seekers**: Automatically respond to recruiters with tailored answers based on your resume.
2. **Busy Professionals**: Save time by letting the bot handle initial recruiter interactions.
3. **Networking**: Maintain professional communication without manual effort.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iklobato/automatic-linkedin-answer-ai.git
   cd automatic-linkedin-answer-ai
   ```

2. **Install Dependencies**:
   ```bash
   uv install 
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file:
     ```bash
     OPENAI_API_KEY=your_openai_api_key
     ```
   - Replace `your_openai_api_key` with your OpenAI API key.

4. **Prepare Documents**:
   - Place your resume and other professional documents in the `docs/` directory.
   - Supported formats: `.txt`.

5. **Configure `config.yaml`**:
   ```yaml
   linkedin:
     username: "your@email.com"
     password: "your_password"
   deepseek:
     api_key: "your_openai_api_key"
     model: "gpt-4o"
   documents_dir: "docs/"
   bot_disclaimer: "🤖 Automated Response: This is an AI assistant. I'll respond based on my resume and experiences."
   ```

---

## **Usage**

1. **Run the Bot**:
   ```bash
   python bot.py
   ```

2. **How It Works**:
   - The bot logs into LinkedIn using your credentials.
   - It navigates to your messages and checks for new recruiter messages.
   - For each new message, it retrieves relevant information from your documents and generates a response using OpenAI's GPT model.
   - The bot sends the response with a disclaimer indicating it's an automated reply.

3. **Monitor Logs**:
   - The bot logs all actions (e.g., new messages, replies, errors) for debugging.
   - Logs are saved in the console with timestamps.

---

## **Customization**

### **1. Add More Documents**
- Place additional `.txt` files in the `docs/` directory.
- The bot will automatically include them in its knowledge base.

### **2. Adjust Response Style**
- Modify the `bot_disclaimer` in `config.yaml` to change the bot's tone.
- Update the `system_prompt` in the `generate_response` function for custom instructions.

### **3. Fine-Tune for Precision**
- Use OpenAI's fine-tuning API to train a custom model on your specific dataset.
- Replace the `ChatOpenAI` model with your fine-tuned model.

---

## **Example Workflow**

1. **Recruiter Message**:
   ```
   Hi, I came across your profile and noticed your experience with Python. Can you tell me more about your projects?
   ```

2. **Bot Response**:
   ```
   🤖 Automated Response: This is an AI assistant. I'll respond based on my resume and experiences.

   I have worked on several Python projects, including a machine learning model for predicting customer churn and a web scraper for data analysis. You can find more details in my resume.
   ```

---

## **Troubleshooting**

### **1. Login Issues**
- Ensure your LinkedIn credentials in `config.yaml` are correct.
- If LinkedIn blocks the login attempt, try using a browser session to verify your account.

### **2. No Responses**
- Check the logs for errors.
- Ensure your documents in the `docs/` directory contain relevant information.

### **3. Rate Limits**
- If OpenAI API rate limits are hit, reduce the bot's polling frequency by increasing the `time.sleep()` duration.

---

## **Contributing**

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- [browser-use](https://github.com/browser-use/browser-use) for browser automation.
- [LangChain](https://langchain.com) for RAG and memory integration.
- [OpenAI](https://openai.com) for the GPT models.

