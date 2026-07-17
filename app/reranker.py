def re_rank(matches, constraints):
    re_ranked = []
    for candidate, score in matches:
        # Simple rule-based boost
        if constraints.get("required_skill") in candidate.get("skills", []):
            score += 0.1
        re_ranked.append((candidate, score))
    return sorted(re_ranked, key=lambda x: x[1], reverse=True)