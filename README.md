# 🚀 Customer Intelligence Platform

An end-to-end AI-powered Customer Intelligence Platform built using **React + .NET + Python AI + PostgreSQL + Qdrant + Llama 3**.

The goal is to build a production-ready intelligent e-commerce platform where AI is integrated into every layer of the application.

---

# Tech Stack

## Frontend
- React
- TypeScript
- Material UI
- Axios

## Backend
- ASP.NET Core 9
- Entity Framework Core
- PostgreSQL
- REST APIs

## AI Service
- Python
- FastAPI
- Sentence Transformers
- HuggingFace
- Ollama
- Llama 3
- Qdrant
- LangChain (Future)
- LangGraph (Future)

---

# Repository Structure

```
CustomerIntelligenceApp

│
├── frontend/                       # React Frontend
│
├── ReviewAnalysisPlatform/    # .NET Backend
│
├── ai-service/                # FastAPI AI Services
│
└── README.md
```

---

# Current Features

## Customer Reviews

Customers can

- Submit reviews
- View reviews
- Rate products
- Recommend products

---

## AI Review Analysis

When a review is submitted,

AI performs

- Sentiment Analysis
- Embedding Generation
- Vector Storage
- Review Similarity Search

---

## Vector Database

Using

- Qdrant

Every review is converted into embeddings and stored.

This enables

- Semantic Search
- Similar Review Search
- RAG

---

## Embedding Model

Using

```
sentence-transformers/all-MiniLM-L6-v2
```

Produces

384-dimensional vectors.

---

## RAG

Implemented

Workflow

```
Question

↓

Embedding

↓

Qdrant Search

↓

Relevant Reviews

↓

Llama 3

↓

Answer
```

---

## LLM

Using

```
Ollama

Llama 3
```

Locally hosted.

---

## Review Ingestion

Added ingestion API

```
POST

/api/ingest/reviews
```

Workflow

```
.NET API

↓

AI Service

↓

Generate Embeddings

↓

Store into Qdrant
```

---

# Current AI Pipeline

```
Customer Review

↓

Sentiment Analysis

↓

Generate Embeddings

↓

Store into Qdrant

↓

Semantic Search

↓

Relevant Reviews

↓

Llama 3

↓

Answer
```

---

# Running the Project

---

# 1. PostgreSQL

Start PostgreSQL

Verify connection

```
localhost:5432
```

Database

```
ReviewAnalysisDB
```

---

# 2. Apply EF Core Migration

Inside

```
ReviewAnalysisPlatform
```

Run

```bash
dotnet ef database update
```

Create migration

```bash
dotnet ef migrations add InitialCreate
```

---

# 3. Run Backend

```bash
cd ReviewAnalysisPlatform

dotnet run
```

Swagger

```
https://localhost:xxxx/swagger
```

---

# 4. Run React App

```
cd app
```

Install

```bash
npm install
```

Run

```bash
npm start
```

or

```bash
npm run dev
```

Depending on your React setup.

---

# 5. Python AI Service

```
cd ai-service
```

Create virtual environment

Mac/Linux

```bash
python3 -m venv .venv
```

Windows

```bash
python -m venv .venv
```

Activate

Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

# 6. Install Ollama

Download

https://ollama.com

Run

```bash
ollama serve
```

Download model

```bash
ollama pull llama3
```

Test

```bash
ollama run llama3
```

---

# 7. Install Qdrant

Docker

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Dashboard

```
http://localhost:6333/dashboard
```

---

# 8. Create Collection

Run

```python
python create_collection.py
```

Collection

```
reviews
```

---

# 9. Ingest Reviews

Call

```
POST

/api/ingest/reviews
```

AI Service fetches reviews from

```
.NET API
```

Generates embeddings

Stores into

```
Qdrant
```

---

# APIs Built

## Review Analysis

```
POST

/api/review/analyze
```

---

## Similar Reviews

```
POST

/api/search
```

---

## RAG

```
POST

/api/rag
```

---

## Review Ingestion

```
POST

/api/ingest/reviews
```

---

# Current Architecture

```
                React

                  │

                  ▼

          ASP.NET Core API

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

 PostgreSQL             AI Service

                            │

          ┌─────────────────┼──────────────────┐

          ▼                 ▼                  ▼

 Sentiment Model     Embedding Model      Llama 3

          │                 │

          └──────────┬──────┘

                     ▼

                  Qdrant

                     │

                     ▼

              Semantic Search

                     │

                     ▼

                  RAG Answer
```

---

# Future Improvements

## Phase 1 - AI Foundation

- Better Sentiment Models
- Aspect Based Sentiment Analysis
- Keyword Extraction
- Named Entity Recognition
- Multi-language Reviews
- Review Summarization
- Spam Detection
- Fake Review Detection

---

## Phase 2 - Advanced RAG

- Hybrid Search (BM25 + Vector Search)
- Metadata Filtering
- Multi-document Retrieval
- Context Compression
- Citation Support
- Product Knowledge Base
- FAQ Knowledge Base

---

## Phase 3 - AI Agents

Implement specialized agents

- Shopping Assistant
- Customer Support Agent
- Product Recommendation Agent
- Review Analysis Agent
- Marketing Agent
- Sales Agent
- Inventory Agent
- Analytics Agent

Using

- LangGraph
- CrewAI
- AutoGen

---

## Phase 4 - MCP Integration

Integrate Model Context Protocol

Tools

- PostgreSQL
- GitHub
- Slack
- Jira
- Email
- Filesystem
- REST APIs
- Vector Databases

Benefits

- Tool calling
- Live database access
- Workflow automation
- External system integration

---

## Phase 5 - Recommendation Engine

Recommend products based on

- Purchase History
- Ratings
- Similar Users
- Similar Products
- Customer Interests
- Browsing Behaviour
- Vector Similarity
- Collaborative Filtering

---

## Phase 6 - Customer Portal

Develop a complete e-commerce portal where customers can:

- Browse products
- Search intelligently using AI
- Receive personalized product recommendations
- Add products to cart
- Checkout securely
- Track orders
- View purchase history
- Submit reviews
- Ask AI questions about products
- Chat with an AI Shopping Assistant
- Receive personalized offers and promotions

---

## Phase 7 - Internal AI Platform

Build AI-powered tools for business users:

### Customer Insights Dashboard

- Customer sentiment trends
- Product popularity
- Complaint analysis
- Review analytics
- Customer segmentation

### AI Support Assistant

- Auto-reply generation
- Ticket summarization
- Knowledge retrieval
- Suggested resolutions

### Marketing AI

- Campaign generation
- Email drafting
- Customer segmentation
- Personalized offers

### Sales AI

- Sales forecasting
- Cross-sell recommendations
- Upsell opportunities
- Lead scoring

### Inventory AI

- Demand prediction
- Stock optimization
- Reorder suggestions

### Executive Dashboard

- AI-generated business insights
- Product performance
- Customer satisfaction metrics
- Revenue trends
- Predictive analytics

---

# Long-Term Vision

The goal is to evolve this project into a production-grade AI-native Customer Intelligence Platform where AI powers every customer interaction and business decision.

Target capabilities include:

- AI-first e-commerce experience
- Intelligent product discovery
- Personalized recommendations
- Conversational shopping assistants
- Enterprise-grade RAG pipelines
- Multi-agent orchestration
- MCP-based tool integration
- Real-time analytics
- Cloud-native deployment on Azure, AWS, or GCP
- Scalable microservices architecture
- CI/CD with GitHub Actions
- Kubernetes-based deployment
- Monitoring with Prometheus and Grafana

---

# Learning Outcomes

This repository demonstrates practical implementation of:

- FastAPI
- ASP.NET Core
- React
- PostgreSQL
- Entity Framework Core
- Sentence Transformers
- Embeddings
- Vector Databases
- Qdrant
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Llama 3 with Ollama
- REST APIs
- AI Service Integration
- Production AI Architecture
- Foundation for AI Agents and MCP

---

# Author

**Ashwini Kumar**

Senior Software Engineer

Building production-grade AI systems with .NET, React, Python, LLMs, RAG, Vector Databases, MCP, and AI Agents.
