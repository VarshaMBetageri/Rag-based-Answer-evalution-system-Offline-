# 🤖 Offline RAG-Based Answer Evaluation System

## 📌 Overview

This project is an AI-powered system that evaluates student answers using an offline **Retrieval-Augmented Generation (RAG)** approach. It combines concepts from Artificial Intelligence, Machine Learning, and Natural Language Processing to provide accurate and efficient answer scoring without using any external APIs.

---

## 🚀 Features

* Fully offline (no API required)
* Context-aware evaluation using RAG
* Semantic similarity using embeddings
* Fast retrieval using FAISS
* Machine Learning-based scoring
* Lightweight and easy to run

---

## 🧠 Workflow

1. User inputs:

   * Question
   * Reference Answer
   * Student Answer

2. System retrieves relevant context from a local knowledge base.

3. Converts all text into embeddings using Sentence Transformers.

4. Computes similarity:

   * Reference vs Student
   * Context vs Student

5. Combines similarity scores.

6. Predicts final score using a trained regression model.

---

## 📁 Project Structure

```
rag_answer_evaluation/
│── app.py
│── train.py
│── rag_utils.py
│── requirements.txt
│
├── data/
│   └── dataset.csv
│
├── models/
│   └── model.pkl
│
└── knowledge_base/
    └── kb.txt
```

---

## ⚙️ Installation

1. Clone or download the project
2. Open in VS Code
3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Train Model

```
python train.py
```

### Step 2: Run Application

```
streamlit run app.py
```

---

## 📊 Example Output

* Retrieved Context: Relevant information from knowledge base
* ML Score: Predicted score (e.g., 8.5/10)

---

## 🔥 Advantages

* No internet required
* Faster execution
* Secure (no data sharing)
* Easy to modify and extend

---

## 🎯 Applications

* Automated answer grading
* Educational tools
* Practice test evaluators
* AI-based learning platforms

---

## 🚀 Future Enhancements

* Add GUI improvements
* Support multiple questions
* Use advanced embedding models
* Integrate database storage

---

## 👨‍💻 Author

Varsha M Betageri

