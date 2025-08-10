# Real Estate Q&A with RAG

This project is a **Real Estate Question Answering system** that uses a **Retrieval-Augmented Generation (RAG)** pipeline to answer questions about property sales data.  
It loads, cleans, preprocesses, enriches, embeds, and retrieves real estate listings to provide accurate and context-based answers.

---

## 📌 Features

- **Automated Data Ingestion**: Loads the real estate dataset from a local file.
- **Data Preprocessing Pipeline**: Cleans missing values, formats columns, and ensures data consistency.
- **Description Enrichment**: Adds AI-generated property descriptions (first 550 rows enriched by default — you can remove the limit in `description_enrichment.py` to enrich all rows).
- **Chunking**: Splits enriched property descriptions for better semantic search.
- **Embeddings**: Generates vector embeddings for each property chunk.
- **Retrieval-Augmented Generation (RAG)**: Retrieves relevant property data and answers user questions.
- **Single Command Execution**: Running `python main.py` will execute the full pipeline end-to-end.



## 📊 Data Source

The dataset originates from **[Kaggle: House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction/data)**.  
We enriched **only the first 550 rows** with AI-generated descriptions for faster testing.  
To enrich the entire dataset, remove or adjust the limit in `description_enrichment.py`.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/osama-jarrar/real-estate-qa.git
cd real-estate-qa
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python main.py
```

This will:

1. Load and preprocess the dataset.
2. Enrich property descriptions.
3. Chunk and embed text.
4. Build a retrieval index.
5. Run the Q\&A system.

---

## 💡 Example Usage

After running `python main.py`, you can interact with the system like:

**User:**

> What is the average price of houses in Bellevue?

**System:**

> Based on our dataset, the average price of houses in Bellevue is around \$...

---

## 🛠 Technologies Used

* **Python 3.9+**
* **Pandas** for data manipulation
* **LangChain** for RAG pipeline
* **OpenAI API** for description generation
* **FAISS** for vector search

---

## 📈 Future Improvements

* Support for additional datasets
* Web-based UI for Q\&A interaction
* More advanced description enrichment
* Fine-tuned model for real estate context

---

## 📜 License

This project is licensed under the MIT License.
