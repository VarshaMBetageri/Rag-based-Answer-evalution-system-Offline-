import streamlit as st
from rag_utils import retrieve_context
from evaluator import evaluate_answer

st.title("📚 Offline RAG Answer Evaluation System")

question = st.text_input("Enter Question")

documents = [
    "Machine learning is a subset of artificial intelligence.",
    "It allows systems to learn from data without explicit programming.",
    "It includes supervised and unsupervised learning."
]

student_answer = st.text_area("Enter Student Answer")

if st.button("Evaluate"):
    context = retrieve_context(question, documents)
    result = evaluate_answer(student_answer, context)

    st.subheader("Retrieved Context")
    st.write(context)

    st.subheader("Evaluation Result")
    st.write(result)