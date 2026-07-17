from pydantic import BaseModel
from typing import List, Dict, Optional

class QueryProfile(BaseModel):
    description: str
    constraints: Optional[Dict] = {}

class MatchResult(BaseModel):
    candidate_id: str
    score: float
    justification: str

class MatchResponse(BaseModel):
    results: List[MatchResult]