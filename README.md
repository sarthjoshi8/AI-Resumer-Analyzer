# 🤖 AI Resume Analyzer

An intelligent resume analysis tool powered by Google Gemini AI. Upload your resume and get instant ATS score, skill gap analysis, keyword suggestions, and tailored improvement recommendations for any job description.

## 🚀 Tech Stack

- **Backend**: Python, FastAPI, Google Gemini API
- **Frontend**: React.js, TailwindCSS, Framer Motion
- **File Parsing**: PyMuPDF (PDF), python-docx (DOCX)
- **AI**: Google Gemini 1.5 Flash
- **Deployment**: Docker, Railway

## ✨ Features

- 📄 Upload PDF/DOCX resume — instant parsing
- 🎯 Paste any job description — AI matches your profile
- 📊 ATS Compatibility Score (0–100)
- 🔑 Keyword gap analysis — missing skills highlighted
- 💡 Section-by-section improvement tips (Experience, Skills, Summary)
- 📈 Before/after preview of improved bullet points
- 💾 Download improved resume as PDF
- 🔒 No data stored — privacy-first design

## 🏗️ Architecture

```
AIResumeAnalyzer/
  app/
    main.py          # FastAPI app entry point
    analyzer.py      # Gemini AI integration
    parser.py        # PDF/DOCX text extraction
    schemas.py       # Pydantic models
  utils/
    scoring.py       # ATS scoring logic
    keywords.py      # Keyword extraction
  static/            # Frontend build output
  templates/         # HTML templates
  Dockerfile
  requirements.txt
```

## ⚙️ Setup

```bash
# Clone and setup
git clone https://github.com/SarthJoshi/ai-resume-analyzer.git
cd ai-resume-analyzer

# Backend
pip install -r requirements.txt
cp .env.example .env   # add GEMINI_API_KEY
uvicorn app.main:app --reload

# Or use Docker
docker build -t resume-analyzer .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key resume-analyzer
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/analyze` | Analyze resume vs JD |
| POST | `/api/parse` | Extract text from resume |
| GET | `/api/health` | Health check |

## 📄 License
- Sarth Hemant Joshi
