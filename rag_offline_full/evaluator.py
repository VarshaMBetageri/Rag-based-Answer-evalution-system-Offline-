from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answer(student, context):
    emb = model.encode([student, context])

    score = cosine_similarity([emb[0]], [emb[1]])[0][0]
    score = round(score * 10, 2)

    if score > 8:
        feedback = "Excellent answer with strong conceptual understanding."
    elif score > 6:
        feedback = "Good answer but missing depth."
    elif score > 4:
        feedback = "Basic understanding, needs improvement."
    else:
        feedback = "Poor answer, lacks relevance."

    return f"Score: {score}/10\nFeedback: {feedback}"