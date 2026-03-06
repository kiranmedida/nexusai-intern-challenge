
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
=======
This repository contains my submission for the NexusAI Internship Challenge. The project simulates a telecom customer support system that combines AI responses, database storage, async data fetching, and escalation decision logic.

The goal of the project is to demonstrate practical backend engineering concepts such as async programming, API integration, database design, concurrency, and rule-based decision systems.

Project Structure
nexusai-intern-challenge

task1/
    message_handler.py

task2/
    schema.sql
    repository.py

task3/
    data_fetcher.py

task4/
    __init__.py
    escalation_engine.py
    test_escalation.py

requirements.txt
README.md
ANSWERS.md

Each task focuses on a different component of the system.

Requirements

Install the required Python libraries using:

pip install -r requirements.txt

Dependencies include:

openai

asyncpg

pytest

python-dotenv

Task 1 – AI Message Handler

This module implements an asynchronous function that processes a customer message and generates a structured AI response.

Function:

handle_message(customer_message, customer_id, channel)

The function:

Calls an AI model to generate a telecom support response

Returns a structured MessageResponse dataclass

Handles important error scenarios:

empty message

API timeout

API rate limit with retry

Formats responses differently depending on the channel (voice vs chat)

Voice responses are limited to short sentences while chat responses can be more descriptive.

Task 2 – Database Schema

A PostgreSQL table named call_records is designed to store all customer interactions.

The schema includes:

customer phone number

communication channel

transcript of the interaction

AI response

resolution outcome

AI confidence score

CSAT score (1–5)

timestamp

interaction duration

Indexes are added to improve query performance when retrieving customer history, recent calls, and resolution statistics.

A Python repository class (CallRecordRepository) provides asynchronous methods to:

store call records

retrieve recent interactions for a customer

Parameterized queries are used to prevent SQL injection.

Task 3 – Parallel Data Fetcher

When a customer contacts support, information must be retrieved from several backend systems.

This task simulates three services:

CRM system (customer account details)

Billing system (payment status)

Ticket history system (previous complaints)

Two approaches are implemented:

Sequential Fetch

Requests are executed one after another.

CRM → Billing → Ticket History

Total time ≈ sum of all delays.

Parallel Fetch

Requests run concurrently using asyncio.gather().

CRM
Billing
Ticket History

Total time ≈ slowest request only.

Example output:

Sequential fetch time ≈ 700ms
Parallel fetch time ≈ 300ms

The billing system also has a 10% simulated failure rate, and the program handles failures gracefully without crashing.

Task 4 – Escalation Decision Engine

This module determines whether an AI response is sufficient or if the issue should be escalated to a human agent.

Function:

should_escalate(context, confidence_score, sentiment_score, intent)

The system implements six escalation rules:

AI confidence below 0.65

Customer sentiment below -0.6

Same complaint repeated three or more times

Service cancellation requests

VIP customer with overdue billing

Incomplete system data with low confidence

Unit tests are written using pytest.

Run the tests with:

pytest task4/ -v
Rule Conflict Handling

In some situations, multiple rules may apply at the same time. The system prioritizes rules that represent high-risk customer scenarios, such as service cancellation or highly negative sentiment. These rules override others because they represent situations where human intervention is most important for customer retention and satisfaction.

For example, even if the AI confidence score is high, a request to cancel service will always trigger escalation. This prioritization ensures that critical cases receive human attention immediately.

Task 5 – Written Design Questions

Detailed design explanations for system decisions are provided in:

ANSWERS.md

These responses discuss topics such as:

handling partial STT transcripts

maintaining knowledge base quality

escalation workflows

future system improvements

Summary

This project demonstrates several backend engineering concepts:

asynchronous Python programming

structured AI integration

database schema design

concurrent data fetching

fault-tolerant service communication

rule-based escalation systems

automated testing with pytest

Together these components simulate a simplified but realistic AI-assisted telecom customer support platform.

