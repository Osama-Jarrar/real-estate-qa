```markdown
# Real Estate Semantic Search System

An **AI-powered semantic search engine** for real estate properties using vector embeddings and similarity search. This project demonstrates how to build an **end-to-end retrieval system** that understands natural language queries and returns relevant properties based on meaning, not just keywords.

> ⚠️ Note: This is a **semantic retrieval system**, not a full RAG. The architecture is designed to be extendable with a generation component for natural language answers.

---

## 🔑 Key Highlights

- **End-to-End AI System**: From raw dataset → preprocessing & enrichment → embeddings → FAISS vector DB → search API → frontend UI.  
- **AI Data Enrichment**: Uses an LLM to auto-generate property descriptions, making listings more natural and searchable.  
- **Semantic Search**: Vector embeddings + FAISS similarity search allow for natural language queries like *“family home near the waterfront”*.  
- **Full-Stack Implementation**:  
  - **Backend**: FastAPI REST API for search.  
  - **Frontend**: Simple HTML/JS search interface for property discovery.  

---

## ⚙️ Architecture

```

Dataset → Preprocessing + AI enrichment → Embeddings → FAISS Vector Store
↓
FastAPI backend (query embedding + retrieval)
↓
Frontend UI (user query → property results)

```

---

## 📌 Features

- ✅ Data preprocessing pipeline  
- ✅ AI description generation (Phi-4)  
- ✅ Vector embeddings (SentenceTransformers)  
- ✅ Similarity search with FAISS  
- ✅ REST API with FastAPI  
- ✅ Simple frontend for search queries  


## 📂 Project Structure

```

real-estate-semantic-search/
├── Data/                  # Processed datasets
├── Data\_ingestion/        # Data loading utilities
├── Data\_preprocessing/    # Data cleaning + enrichment
├── retrieval/             # Vector search components
│   ├── embedding.py       # Embedding generation
│   ├── retrieve.py        # FAISS similarity search
│   └── pipeline.py        # Search pipeline
├── front\_end/             # Web interface
├── utils/                 # Model loading utilities
├── vector\_store/          # FAISS vector database
└── main.py                # FastAPI backend

````

---

## 📊 Dataset

- **Source**: King County House Sales Data  
- **Size**: ~1,289 properties (subset of 550 used)  
- **Features**: Price, bedrooms, bathrooms, square footage, location, condition, grade  
- **AI Enrichment**: Generated property descriptions  

---

## 🔮 Future Improvements

- Add LLM generation layer → full RAG system (answers + explanations).  
- Improve ranking with hybrid search (dense + sparse).  
- Add configuration management, error handling, and Docker deployment.  

---

## 🎯 Learning Outcomes

This project demonstrates:  
- How to build semantic retrieval systems with embeddings + FAISS.  
- How to integrate LLMs into data pipelines for enrichment.  
- How to deliver a full-stack AI project (backend + frontend).  
- How to structure a project for extensibility (towards RAG).  

---

## 🛠️ Installation & Usage

```bash
git clone <repo-url>
cd real-estate-semantic-search
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
````

Then open `front_end/index.html` in your browser and try natural language property searches.

---

```

---
