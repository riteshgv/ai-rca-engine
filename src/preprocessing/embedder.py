from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    """
    Converts chunks of logs into embeddings.
    Each chunk becomes one vector representation.
    """
    chunk_texts = [
        "\n".join([log["message"] for log in chunk])
        for chunk in chunks
    ]

    embeddings = model.encode(chunk_texts)
    return np.array(embeddings)

