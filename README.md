# Hellobooks AI Assistant (RAG System)

## Overview

This project is a prototype AI assistant for **Hellobooks**, an AI-powered bookkeeping platform.

The assistant answers **basic accounting questions** using a **Retrieval-Augmented Generation (RAG)** architecture.
Instead of relying only on a language model, the system retrieves relevant accounting documents from a knowledge base and uses them as context to generate accurate responses.

---

## Features

* Small **accounting knowledge base**
* **Embedding generation** using HuggingFace models
* **Vector similarity search** using FAISS
* **Retrieval-Augmented Generation (RAG)** pipeline
* **LLM-generated answers**
* **Docker support** for easy deployment

---

## Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* HuggingFace Sentence Transformers
* OpenAI LLM API
* Docker

---

## Project Structure

```
nexusai-intern-challenge
│
├── data
│   ├── bookkeeping.md
│   ├── invoices.md
│   ├── profit_loss.md
│   ├── balance_sheet.md
│   └── cash_flow.md
│
├── rag_system.py
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

### File Descriptions

**data/**
Contains accounting documents used as the knowledge base.

**rag_system.py**
Implements the RAG pipeline:

* Load documents
* Generate embeddings
* Store vectors in FAISS
* Retrieve relevant context

**app.py**
Command-line interface for asking questions to the AI assistant.

---

## Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/kiranmedida/nexusai-intern-challenge.git
cd nexusai-intern-challenge
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Set OpenAI API key

```
export OPENAI_API_KEY="your_api_key_here"
```

(Windows)

```
set OPENAI_API_KEY=your_api_key_here
```

### 4️⃣ Run the application

```
python app.py
```

---

## Example

```
Hellobooks AI Assistant

Question: What is a balance sheet?

Answer:
A balance sheet is a financial statement that shows a company's financial position by listing its assets, liabilities, and equity.
```

---

## RAG Workflow

User Question
↓
Retrieve relevant accounting documents from vector database
↓
Provide retrieved context to LLM
↓
Generate final answer

---

## Running with Docker

### Build Docker Image

```
docker build -t hellobooks-ai .
```

### Run Container

```
docker run -it hellobooks-ai
```

---

## Future Improvements

* Add a web interface using **Streamlit**
* Expand accounting knowledge base
* Improve document chunking and retrieval
* Add conversational memory

---

## Author

Surya Kiran
