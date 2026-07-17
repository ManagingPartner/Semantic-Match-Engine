from sentence_transformers import SentenceTransformer
import numpy as np

# Use a multilingual model to satisfy the JD requirement
model = SentenceTransformer('intfloat/multilingual-e5-base')

def embed(text: str) -> np.ndarray:
    vec = model.encode(text)
    return vec / np.linalg.norm(vec) # Normalize for cosine similarity