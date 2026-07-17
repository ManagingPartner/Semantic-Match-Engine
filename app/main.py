from fastapi import FastAPI
from app.schemas import QueryProfile, MatchResponse
from app.embedding_service import embed
# ... remove all leading dots from your imports
from app.index_store import IndexStore
from app.reranker import re_rank
from app.justifier import generate_justification

app = FastAPI()
store = IndexStore()

@app.post("/match", response_model=MatchResponse)
async def match(query: QueryProfile):
    query_vec = embed(query.description)
    raw_matches = store.search(query_vec)
    ranked = re_rank(raw_matches, query.constraints)
    
    results = [
        {"candidate_id": c['id'], "score": s, "justification": generate_justification(c, query)}
        for c, s in ranked
    ]
    return {"results": results}