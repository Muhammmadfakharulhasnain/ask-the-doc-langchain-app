# 🦜🔗 Ask the Doc App

Ask-the-Doc is a powerful and interactive Q&A tool built with **Streamlit**, **LangChain**, and **OpenAI GPT**. Simply upload a `.pdf`, `.docx`, or `.txt` file and ask questions about its content in natural language. The app uses vector-based search and retrieval-augmented generation (RAG) to provide relevant answers based on your query.

## 🚀 Features

- 🔍 Upload and parse PDF, DOCX, and TXT files
- 🧠 Extract content using LangChain's `CharacterTextSplitter`
- 💡 Generate semantic embeddings using `OpenAIEmbeddings`
- 📚 Perform document search with Chroma vector store
- 🤖 Ask questions using a RetrievalQA chain with OpenAI's language model
- 🌐 Simple UI built with Streamlit

## 🖼️ Demo

![App Screenshot](https://via.placeholder.com/800x400.png?text=Ask+the+Doc+App+Screenshot) <!-- Replace with actual screenshot URL -->

## 📦 Dependencies

Install the required packages:

```bash
pip install streamlit langchain openai chromadb PyPDF2 python-docx


## 🔑 Setup

Clone the repository:

```bash
git clone https://github.com/your-username/ask-the-doc-langchain-app.git
cd ask-the-doc-langchain-app
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Input your **OpenAI API Key** when prompted.

## 📁 Project Structure

```bash
ask-the-doc-langchain-app/
├── app.py                # Main Streamlit application
├── README.md             # Project documentation
└── requirements.txt      # Optional: list of dependencies
```

## ✅ To-Do

* [ ] Add support for more file types (e.g., HTML, CSV)
* [ ] Allow chat history memory
* [ ] Option to download summary or answers
* [ ] Dockerize the app

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify.

Made with ❤️ using LangChain, OpenAI, and Streamlit.
