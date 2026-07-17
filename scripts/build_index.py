import json
import numpy as np
from app.embedding_service import embed

def build_index():
    # Load raw candidates
    with open('data/candidates.json', 'r') as f:
        candidates = json.load(f)

    # Generate embeddings for each candidate
    print(f"Embedding {len(candidates)} candidates...")
    for candidate in candidates:
        # Concatenate text fields for embedding
        text_to_embed = f"{candidate['summary']} {' '.join(candidate['skills'])}"
        candidate['embedding'] = embed(text_to_embed).tolist()

    # Save the updated candidates with embeddings
    with open('data/candidates.json', 'w') as f:
        json.dump(candidates, f, indent=4)
    
    print("Index build complete! Data saved to data/candidates.json.")

if __name__ == "__main__":
    build_index()