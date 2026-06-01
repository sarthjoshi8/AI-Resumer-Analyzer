import google.generativeai as genai
import os
import json
from app.schemas import AnalysisResult

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class ResumeAnalyzer:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    async def analyze(self, resume_text: str, job_description: str) -> AnalysisResult:
        prompt = f"""
You are an expert ATS (Applicant Tracking System) and career coach.

Analyze the following resume against the job description and return a JSON response with exactly this structure:
{{
  "ats_score": <integer 0-100>,
  "summary": "<2 sentence overall assessment>",
  "matched_keywords": ["keyword1", "keyword2"],
  "missing_keywords": ["keyword1", "keyword2"],
  "strengths": ["strength1", "strength2", "strength3"],
  "improvements": [
    {{"section": "Experience", "issue": "...", "suggestion": "..."}},
    {{"section": "Skills", "issue": "...", "suggestion": "..."}}
  ],
  "improved_bullets": [
    {{"original": "...", "improved": "..."}}
  ]
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY the JSON, no markdown or explanation.
"""
        response = self.model.generate_content(prompt)
        raw = response.text.strip().strip("```json").strip("```")
        data = json.loads(raw)
        return AnalysisResult(**data)
