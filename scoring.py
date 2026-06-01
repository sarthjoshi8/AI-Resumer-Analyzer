import re
from typing import List

POWER_WORDS = [
    "achieved", "built", "designed", "developed", "implemented", "improved",
    "increased", "led", "managed", "optimized", "reduced", "scaled", "delivered"
]

def score_resume(text: str, job_keywords: List[str]) -> dict:
    text_lower = text.lower()
    matched = [kw for kw in job_keywords if kw.lower() in text_lower]
    keyword_score = (len(matched) / len(job_keywords)) * 40 if job_keywords else 0

    power_count = sum(1 for w in POWER_WORDS if w in text_lower)
    action_score = min(power_count * 3, 20)

    has_quantification = bool(re.search(r'\d+%|\d+x|\$\d+|\d+ (users|people|teams|projects)', text_lower))
    quant_score = 20 if has_quantification else 0

    sections = ['experience', 'education', 'skills', 'projects']
    section_score = sum(5 for s in sections if s in text_lower)

    total = int(keyword_score + action_score + quant_score + section_score)
    return {
        "total": min(total, 100),
        "breakdown": {
            "keywords": round(keyword_score),
            "action_verbs": action_score,
            "quantification": quant_score,
            "sections": section_score,
        }
    }
