# Semantic Match Engine

A compute-efficient, domain-agnostic engine designed to rank candidate items against natural-language query profiles. The system uses dense vector representations for semantic understanding and rule-based logic for attribute-aware re-ranking.

## ✨ Key Features
* **Multilingual Semantic Search**: Uses `multilingual-e5-base` to enable cross-lingual matching (e.g., querying in Hindi or English against a mixed-language pool)[cite: 1].
* **Attribute-Aware Re-ranking**: Combines raw semantic similarity with structured, rule-based boosting/filtering to ensure matches meet specific constraints (e.g., age, skills, language)[cite: 1].
* **Explainable Matching ("Copilot" Layer)**: Instead of a black-box score, the system provides per-match justifications, identifying specific attribute overlaps to assist human decision-making[cite: 1].
* **Production-Ready Architecture**: Built with a stateless pipeline and modular FastAPI design for easy scalability[cite: 1].

## 🛠️ Tech Stack
* **Language**: Python 3.11+
* **API Framework**: FastAPI, Uvicorn
* **Embeddings**: Sentence-Transformers (`multilingual-e5-base`)
* **Validation**: Pydantic V2

## ⚙️ Quickstart
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
