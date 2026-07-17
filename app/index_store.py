import numpy as np
import json

class IndexStore:
    def __init__(self, data_path="data/candidates.json"):
        with open(data_path, 'r') as f:
            self.candidates = json.load(f)
        self.embeddings = np.array([c['embedding'] for c in self.candidates])

    def search(self, query_vec: np.ndarray, top_k=5):
        scores = np.dot(self.embeddings, query_vec)
        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [(self.candidates[i], float(scores[i])) for i in top_indices]