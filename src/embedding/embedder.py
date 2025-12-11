# src/embedding/embedder.py

from sentence_transformers import SentenceTransformer

class LogEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, chunks):
        """
        chunks: list of text blocks (list[str])
        returns list of vectors
        """
        return self.model.encode(chunks, convert_to_numpy=True)

