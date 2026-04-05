# Offline RAG Answer Evaluation System

## Overview
This project implements a simplified Retrieval-Augmented Generation (RAG) system offline.

## Components
1. Retriever (TF-IDF based)
2. Context Selection
3. Answer Evaluation (Similarity + Rule-based)

## Workflow
Query -> Retrieve context -> Evaluate answer

## Run
pip install -r requirements.txt
python app.py

## Output
- Retrieved context
- Score
- Feedback

## Future Improvements
- Use BERT embeddings
- Add vector DB (FAISS)
- Add UI (Streamlit)
