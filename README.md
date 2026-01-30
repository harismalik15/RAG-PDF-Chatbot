# 🤖 PDF-Talk: Intelligent RAG Chatbot


**PDF-Talk** is a professional-grade AI assistant that allows users to have meaningful conversations with their PDF documents. It leverages **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers using Google's Gemini Flash model and ChromaDB as a vector store.



## 🌟 Key Features
- **Smart Document Parsing:** Efficiently extracts and chunks text from PDFs.
- **Contextual Retrieval:** Uses Google's `text-embedding-004` to find the most relevant information.
- **Persistent Memory:** Saves your document's brain locally in ChromaDB, so you don't have to re-process files.
- **Hallucination Guard:** Strictly follows the provided context to ensure factual accuracy.
- **Interactive CLI:** A seamless terminal-based chat interface.

## 🛠️ Tech Stack
- **LLM:** Google Gemini 2.0 Flash
- **Embeddings:** Google Generative AI Embeddings
- **Vector Database:** ChromaDB (Persistent)
- **PDF Engine:** PyPDF

---

## ⚙️ Installation & Setup

### 1. Clone the Project
```bash
git clone [https://github.com/harismalik15/RAG-PDF-Chatbot.git](https://github.com/harismalik15/RAG-PDF-Chatbot.git)
cd RAG-PDF-Chatbot
```

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
- **Prepare Data:** Place your PDF in the project folder and name it customer_care.pdf (or update the path in main.py).
- **Initialize & Chat:** 
```bash
python main.py
```
- **Ask Questions:** Type your queries in the terminal. Type q to quit the session.

## 📁 Project Structure
- **Prepare Data:** main.py The entry point that orchestrates the entire pipeline.
- **pdf_reader.py:** Handles PDF text extraction.
- **chunking.py:** Breaks text into optimized overlapping segments.
- **embeddings.py:** Generates vector embeddings via Google API.
- **vector_db.py:** Manages the local ChromaDB storage and similarity search.
- **rag_engine.py:** Handles the prompt engineering and Gemini response generation.
 






