from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_context(query, documents):
    query_emb = model.encode([query])
    doc_emb = model.encode(documents)

    similarities = cosine_similarity(query_emb, doc_emb)[0]
    best_index = similarities.argmax()

    return documents[best_index]
