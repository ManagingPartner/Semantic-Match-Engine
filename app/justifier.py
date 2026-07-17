def generate_justification(candidate: dict, query: dict) -> str:
    """
    Generates a human-readable string explaining why a candidate matched.
    """
    matched_skills = [s for s in candidate.get("skills", []) if s in str(query.get("description", ""))]
    
    # Generate a simple, deterministic justification
    justification = f"Matched on: Skills overlap {matched_skills}. "
    justification += f"Language proficiency: {', '.join(candidate.get('languages', []))}."
    
    return justification