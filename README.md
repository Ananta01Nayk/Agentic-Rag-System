# 🚀 Agentic RAG System

An intelligent Agentic Retrieval-Augmented Generation (RAG) system built using **FastAPI, React, ChromaDB, LangGraph, and Large Language Models (LLMs)**. The application provides accurate, context-aware answers by combining document retrieval, relevance validation, iterative web search, and AI-powered reasoning.

---

## 📌 Project Overview

Traditional RAG systems rely solely on retrieved document chunks, which may lead to inaccurate answers when the retrieved context is irrelevant or incomplete.

This project introduces an **Agentic AI Workflow** that validates retrieved information before generating responses. When document retrieval fails, the system automatically performs web searches, validates the results, and iteratively refines search queries until relevant information is found.

This approach significantly improves answer quality and reduces hallucinations.

---

## ✨ Key Features

### 📄 Document-Based Question Answering

* PDF document ingestion
* Text extraction and chunking
* Vector embedding generation
* ChromaDB vector storage
* Semantic similarity search

### 🤖 Agentic AI Workflow

* Intelligent query routing
* Context relevance validation
* Automated query rewriting
* Multi-step reasoning
* Dynamic decision making

### 🌐 Web Search Integration

* Tavily Search integration
* Automatic fallback when document retrieval fails
* Query optimization for better search results
* Multi-iteration web retrieval

### 🛡️ Hallucination Reduction

* Relevance checking before answer generation
* Context grounding
* Iterative search refinement
* Validation-based workflow

### 🎨 Modern Frontend

* React-based chat interface
* Real-time AI responses
* Responsive design
* User-friendly experience

---

# 🏗️ System Architecture

```text
User Question
      │
      ▼
Document Retrieval (ChromaDB)
      │
      ▼
Relevance Check
      │
 ┌────┴────┐
 │         │
Yes        No
 │          │
 ▼          ▼
Generate   Query Generator
Answer         │
               ▼
        Tavily Web Search
               │
               ▼
        Relevance Check
               │
      ┌────────┴────────┐
      │                 │
     Yes                No
      │                 │
      ▼                 ▼
Generate         Generate New
Answer           Search Query
      │
      ▼
Return Response
```

---

# ⚙️ How It Works

## Step 1: User Question

The user submits a question through the React frontend.

Example:

```text
What is Retrieval-Augmented Generation?
```

---

## Step 2: Vector Retrieval

The system:

* Converts the question into embeddings
* Searches ChromaDB
* Retrieves the most relevant document chunks

```text
User Query
    ↓
Embedding
    ↓
ChromaDB Search
    ↓
Retrieved Context
```

---

## Step 3: Relevance Validation

Instead of immediately generating an answer, an AI relevance-checking node evaluates whether the retrieved context actually answers the user's question.

### If Relevant

```text
Retrieved Context
       ↓
Answer Generation
```

### If Not Relevant

```text
Retrieved Context
       ↓
Query Generator Node
```

---

## Step 4: Query Generation

The Agent generates a search-optimized query designed for web retrieval.

Example:

```text
User Question:
What is Agentic AI?

Generated Search Query:
Latest explanation of Agentic AI systems and applications
```

---

## Step 5: Web Search

The generated query is sent to Tavily Search.

```text
Generated Query
       ↓
Tavily Search
       ↓
Web Results
```

---

## Step 6: Web Context Validation

The retrieved web content is checked again for relevance.

### Relevant

```text
Web Context
      ↓
Answer Generation
```

### Not Relevant

```text
Web Context
      ↓
Generate Better Query
      ↓
Search Again
```

The system repeats this loop until useful context is found.

---

## Step 7: LLM Answer Generation

Once reliable context is available, the LLM generates a response using:

* User Question
* Retrieved Document Context
* Web Search Context
* Agentic Reasoning Workflow

```text
Question
    +
Context
    +
Reasoning
    ↓
Generated Answer
```

---

## 🎯 Why This Architecture?

Unlike traditional chatbots, this system does not blindly trust retrieved information.

Benefits:

✅ Reduces hallucinations

✅ Improves answer accuracy

✅ Handles missing document information

✅ Supports real-time web knowledge

✅ Performs intelligent search refinement

✅ Produces context-grounded responses

---

# 🛠️ Technology Stack

## Backend

* FastAPI
* Python
* LangGraph
* LangChain
* ChromaDB
* Tavily Search
* Uvicorn

## Frontend

* React.js
* Axios
* CSS

## AI Components

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Vector Search
* Agentic AI Workflow
* Query Rewriting
* Context Validation

---

# 📂 Project Structure

```bash
rag_fastAPI/
│
├── backend/
│   ├── chroma_db/
│   ├── data/
│   ├── ingest.py
│   ├── retriever.py
│   ├── retrieve2.py
│   ├── relevant.py
│   ├── direct_generate.py
│   ├── generate_from_context.py
│   ├── prompts.py
│   ├── rag_graph.py
│   ├── router_node.py
│   ├── state.py
│   ├── web_search.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── Chat.js
│   │   ├── Chat.css
│   │   ├── App.js
│   │   └── App.css
│   ├── package.json
│   └── package-lock.json
│
└── README.md
```

---

# 🚀 Installation

## Backend Setup

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run React App:

```bash
npm start
```

Frontend URL:

```bash
http://localhost:3000
```

---

# 🔮 Future Enhancements

* Multi-PDF support
* Memory-enabled conversations
* Citation generation
* Multi-agent architecture
* Streaming responses
* Authentication system
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)

---

# 👨‍💻 Author

### Ananta Nayak

AI/ML Engineer | Data Science Enthusiast | Full Stack Developer

Interested in:

* Agentic AI
* Generative AI
* RAG Systems
* Machine Learning
* Deep Learning
* Full Stack Development

---

# 📜 License

This project is licensed under the MIT License.
