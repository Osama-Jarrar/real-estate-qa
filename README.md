# Real Estate Semantic Search System

An **AI-powered semantic search engine** for real estate properties using vector embeddings and similarity search. This project demonstrates how to build an **end-to-end retrieval system** that understands natural language queries and returns relevant properties based on meaning, not just keywords.

> ⚠️ **Important Note**: This is a **semantic retrieval system**, not a full RAG (Retrieval-Augmented Generation) system. While the architecture is designed to be extendable with a generation component, it currently focuses on intelligent property retrieval rather than natural language answer generation.

---

## 🔑 Key Highlights

- **End-to-End AI System**: From raw dataset → preprocessing & enrichment → embeddings → FAISS vector DB → search API → frontend UI
- **AI Data Enrichment**: Uses an LLM to auto-generate property descriptions, making listings more natural and searchable
- **Semantic Search**: Vector embeddings + FAISS similarity search allow for natural language queries like *"family home near the waterfront"*
- **Full-Stack Implementation**: Complete backend (FastAPI) + frontend (HTML/JS) with semantic search capabilities
- **Production-Ready Architecture**: Designed with extensibility in mind for future RAG implementation

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

## 📌 What This Project Actually Is

- **Semantic Property Search**: Users can search for properties using natural language descriptions
- **Vector-Based Retrieval**: Uses embeddings to find similar properties based on query meaning
- **Data Enrichment Pipeline**: Automatically generates property descriptions using AI
- **Web Interface**: Simple search interface for property discovery

## ❌ What This Project Is NOT

- **Not a RAG system** (missing LLM generation of natural language responses)
- **Not a property listing site** (focused on search, not browsing)
- **Not a chatbot** (no conversational AI)
- **Not a property valuation tool** (no price predictions)

---

## 🚀 Features

### ✅ Implemented
- **Data Preprocessing Pipeline**: Cleans and transforms raw property data
- **AI Description Generation**: Uses Phi-4 model to create property descriptions
- **Vector Embeddings**: Converts properties to embeddings using sentence-transformers
- **Similarity Search**: FAISS-based vector search with scoring
- **Web API**: FastAPI backend for search queries
- **Frontend Interface**: Simple HTML/JS search interface

### 🔮 Future Enhancements (To Make It True RAG)
- **LLM Response Generation**: Natural language answers to user queries
- **Query Understanding**: Explanation of why properties were selected
- **Result Summarization**: Intelligent summarization of search results
- **Conversational Interface**: Follow-up question handling

---

## 📂 Project Structure

```
real-estate-semantic-search/
├── Data/                  # Processed datasets
├── Data_ingestion/        # Data loading utilities
├── Data_preprocessing/    # Data cleaning + enrichment
├── rag/                  # Vector search components
│   ├── chunking.py       # Document chunking
│   ├── embedding.py      # Embedding generation
│   ├── retrieve.py       # FAISS similarity search
│   └── rag_pipeline.py   # Search pipeline
├── front_end/            # Web interface
├── utils/                # Model loading utilities
├── vector_store/         # FAISS vector database
└── main.py               # FastAPI backend
```

---

## 📊 Dataset

- **Source**: King County House Sales Data
- **Size**: ~1,289 properties (subset of 550 used for processing)
- **Features**: Price, bedrooms, bathrooms, square footage, location, condition, grade, etc.
- **AI Enrichment**: Generated property descriptions for enhanced searchability

---

## 🛠️ Technical Implementation

### Embedding Model
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Database**: FAISS for fast similarity search
- **Chunking**: Property-level chunks (one chunk per property)

### AI Description Generation
- **Model**: Phi-4 (quantized)
- **Purpose**: Generate property descriptions from features
- **Batch Processing**: Processes 25 properties at a time
- **Checkpointing**: Saves progress during long processing runs

### Search Algorithm
- **Similarity Metric**: Cosine similarity
- **Score Normalization**: MinMax scaling (0-1 range)
- **Filtering**: Only returns results with score > 0.5
- **Default Results**: Top 5 most similar properties

---

## 🚀 Installation & Usage

### Quick Start
```bash
git clone <repo-url>
cd real-estate-semantic-search
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Running the System
1. **Start the backend**: `python main.py`
2. **Open the frontend**: Navigate to `front_end/index.html` in your browser
3. **Search for properties**: Type natural language queries like:
   - "3 bedroom house near waterfront"
   - "affordable family home with good condition"
   - "modern house with excellent view"

---

## 🎯 Learning Outcomes & Technical Skills Demonstrated

This project showcases:

- **AI/ML Engineering**: Vector embeddings, similarity search, LLM integration
- **Data Engineering**: End-to-end data pipeline, preprocessing, enrichment
- **Backend Development**: FastAPI, REST APIs, vector databases
- **Frontend Development**: HTML/JS, search interfaces, user experience
- **System Architecture**: Modular design, extensibility, production considerations
- **DevOps**: Basic Development Setup: Virtual environments, dependency installation, local model loading

---

## 🔮 Future Roadmap

### Phase 1: Add Generation Component (True RAG)
- [ ] Integrate LLM for query response generation
- [ ] Add result summarization and explanation
- [ ] Implement conversational follow-up handling

### Phase 2: Enhanced Search
- [ ] Query understanding and refinement
- [ ] Multi-modal search (images, maps)
- [ ] Advanced filtering and sorting options

### Phase 3: Production Features
- [ ] Property comparison tools
- [ ] Market analysis and trends

---

## 📋 Current Limitations & Technical Debt

### Limitations
1. **No True RAG**: Missing LLM generation of natural language responses
2. **Limited Dataset**: Only processes first 550 properties from original dataset
3. **Basic Scoring**: Simple similarity scoring without advanced ranking
4. **No Query Expansion**: Doesn't expand or refine user queries

### Technical Debt
- **Hardcoded Paths**: Some file paths are hardcoded
- **Error Handling**: Limited error handling in several components
- **Configuration**: No configuration file for model paths and parameters
- **Logging**: Minimal logging and debugging information

---

## 🤝 Contributing

This project serves as a learning example for:
- Building vector search systems
- Implementing data preprocessing pipelines
- Creating AI-powered data enrichment
- Building semantic search interfaces

Contributions are welcome, especially to address the limitations mentioned above and move towards a true RAG system.



## 🙏 Acknowledgments

- King County House Sales Dataset
- Sentence Transformers for embeddings
- FAISS for vector similarity search
- FastAPI for the web backend
- Microsoft Phi-4 for description generation
