# PDF Chatbot with Google Gemini AI

A Streamlit-based chatbot that allows users to upload PDF documents and ask questions about their content. Built with LangChain and powered by Google's Gemini 2.0 AI model.

## 🚀 Features

- **PDF Upload**: Upload any PDF document through a simple web interface
- **Intelligent Q&A**: Ask questions about the document content and get accurate answers
- **Semantic Search**: Uses vector embeddings to find relevant information from your documents
- **Real-time Processing**: Instant responses powered by Google Gemini 2.0
- **Privacy-Focused**: Process sensitive documents locally without sending data to public AI services

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI/ML**: LangChain, Google Gemini 2.0
- **Vector Store**: FAISS
- **PDF Processing**: PyPDF2
- **Embeddings**: Google Generative AI Embeddings
- **Language**: Python

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI Studio API key

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd pdf-chatbot
   ```

2. **Install required packages**
   ```bash
   pip install streamlit PyPDF2 langchain langchain-google-genai faiss-cpu google-generativeai
   ```

3. **Set up your API key**
   
   Create an `env.json` file in the root directory:
   ```json
   {
     "GOOGLE_API_KEY": "your_google_api_key_here"
   }
   ```

4. **Get your Google AI Studio API key**
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Sign in with your Google account
   - Click "Get API Key"
   - Create a new API key for your project
   - Copy the key to your `env.json` file

## 🚀 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Upload a PDF**
   - Use the sidebar to upload your PDF document
   - The app will automatically process and chunk the text

3. **Ask questions**
   - Type your question in the input field
   - Get instant answers based on your document content

## 📁 Project Structure

```
pdf-chatbot/
│
├── app.py              # Main Streamlit application
├── env.json            # API key configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔍 How It Works

1. **PDF Processing**: Extracts text from uploaded PDF using PyPDF2
2. **Text Chunking**: Splits document into manageable chunks using RecursiveCharacterTextSplitter
3. **Embeddings**: Converts text chunks into vector embeddings using Google's embedding model
4. **Vector Store**: Stores embeddings in FAISS for efficient similarity search
5. **Question Answering**: Uses similarity search to find relevant chunks and Google Gemini 2.0 to generate answers

## ⚙️ Configuration

You can modify these parameters in the code:

```python
# Text chunking parameters
chunk_size = 1000      # Size of each text chunk
chunk_overlap = 150    # Overlap between chunks

# LLM parameters
temperature = 0        # Response randomness (0 = deterministic)
max_tokens = 5000     # Maximum response length
```

## 🔒 Privacy & Security

- Documents are processed locally on your machine
- No data is sent to external services except for AI processing
- Perfect for sensitive/confidential documents
- Google's API is used only for AI inference, not data storage

## 🚨 Limitations

- Only supports PDF files currently
- Large documents may take time to process
- Response quality depends on document structure and content
- Requires internet connection for AI processing

## 🔮 Future Enhancements

- [ ] Support for multiple file formats (Word, PowerPoint, etc.)
- [ ] Conversation memory/history
- [ ] Batch processing of multiple documents
- [ ] Advanced filtering and search options
- [ ] Export chat history

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI orchestration framework
- [Google AI Studio](https://aistudio.google.com/) for the Gemini API
- [Streamlit](https://streamlit.io/) for the web interface
- [FAISS](https://github.com/facebookresearch/faiss) for vector search

## 📧 Contact

Your Name - dulanmherath@outlook.com


---

⭐ Star this repository if you found it helpful!
