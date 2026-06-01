from pydantic import BaseModel
from typing import List, Optional

class Improvement(BaseModel):
    section: str
    issue: str
    suggestion: str

class BulletImprovement(BaseModel):
    original: str
    improved: str

class AnalysisResult(BaseModel):
    ats_score: int
    summary: str
    matched_keywords: List[str]
    missing_keywords: List[str]
    strengths: List[str]
    improvements: List[Improvement]
    improved_bullets: Optional[List[BulletImprovement]] = []
