<img width="1376" height="768" alt="Gemini_Generated_Image_2cvuvf2cvuvf2cvu" src="https://github.com/user-attachments/assets/d177d8cf-6d25-48fb-9795-5840b1c98b4c" />
#AI Medical Chatbot with RAG & Medical Report Analysis

An AI-powered Medical Chatbot that combines **Retrieval-Augmented Generation (RAG)** with **Medical Report Analysis** to help users understand medical documents, laboratory reports, and medicine-related information. The application leverages **Large Language Models (LLMs)** to provide intelligent responses, analyze laboratory reports, and generate simplified health summaries.

---

## 📌 Project Overview

The AI Medical Chatbot enables users to:

- 📄 Upload medical documents (PDF, TXT, DOCX)
- 💬 Ask questions about uploaded documents using RAG
- 🩺 Analyze laboratory test reports automatically
- 📊 Extract laboratory test values from different report formats
- 💊 Provide medicine-related information
- ⚠️ Explain abnormal laboratory findings in simple language
- 🌍 Support multiple medical report types
- 📝 Generate AI-based medical report summaries

---

## ✨ Features

### 🤖 Retrieval-Augmented Generation (RAG)

- Upload medical documents
- Semantic document search
- Context-aware question answering
- HuggingFace Embeddings
- FAISS Vector Database
- Llama 3.2 via Ollama

---

### 🧪 Medical Report Analysis

- Automatic laboratory report parsing
- Extraction of medical test values
- Identification of abnormal findings
- Health summary generation
- Easy-to-understand explanations

---

### 💊 Medicine Information

- Medicine details lookup
- Uses and indications
- Side effects
- Composition
- Manufacturer information

---

### 🌐 Additional Features

- Multi-document support
- OCR support for scanned/image reports
- AI-generated medical summaries
- Interactive Streamlit interface

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
          Streamlit Web App
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
 Document Upload      User Question
        │                   │
        ▼                   ▼
 Document Loader      Similarity Search
        │                   │
        ▼                   ▼
 Text Splitter        FAISS Vector Store
        │                   │
        ▼                   ▼
 HuggingFace Embeddings
                  │
                  ▼
             Llama 3.2 (Ollama)
                  │
                  ▼
          AI Generated Response

```

---

# 🎯 Objectives

- Build an AI-powered medical assistant.
- Implement Retrieval-Augmented Generation (RAG) for medical question answering.
- Automatically analyze laboratory reports.
- Extract laboratory test values from multiple report formats.
- Detect abnormal laboratory findings.
- Generate AI-powered medical summaries.
- Simplify complex medical information for users.

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## AI & Large Language Models

- LangChain
- Ollama
- Llama 3.2

## RAG Components

- HuggingFace Embeddings
- FAISS Vector Database

## Document Processing

- PyMuPDF
- PDF Reader
- OCR (Image Report Support)

## Medical Report Analysis

- Regular Expressions (Regex)
- Python Dictionaries
- Medical Report Parser

## Report Generation

- PDF Report Generator

---

# 📂 Project Structure

```
AI-Medical-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   ├── report_parser.py
│   ├── report_analyzer.py
│   ├── report_reader.py
│   ├── medicine.py
│   └── language.py
│
├── data/
│   ├── medical_documents/
│   └── medicine_database.csv
│
└── reports/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Medical-Chatbot.git
```

Navigate to the project

```bash
cd AI-Medical-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🚀 How It Works

1. Upload one or more medical documents.
2. Documents are processed and converted into embeddings.
3. Embeddings are stored in a FAISS Vector Database.
4. User submits a medical question.
5. Relevant document chunks are retrieved.
6. Llama 3.2 generates a context-aware response.
7. Laboratory reports are parsed and analyzed.
8. The chatbot explains abnormal findings and provides AI-generated summaries.

---

# 📸 Screenshots

> Add screenshots of your application here.

- Home Page
- Document Upload
- Chat Interface
- Medical Report Analysis
- AI Generated Summary

---

# 🔮 Future Enhancements

- Voice-enabled chatbot
- Medical image analysis
- Doctor appointment recommendations
- Drug interaction detection
- Personalized health recommendations
- Cloud deployment
- User authentication
- Medical history tracking

---

# ⚠️ Disclaimer

This project is intended **for educational and research purposes only**. It does **not** replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

---

# 👩‍💻 Author

**Ritika Jha**

- B.Tech Computer Science Engineering
- AI | Machine Learning | Generative AI | NLP | RAG
- Passionate about building AI-powered healthcare applications.

---

## ⭐ If you found this project helpful, consider giving it a Star on GitHub!
