# 🎓 AI Career Mentor for Students

An intelligent platform that helps students identify career paths, detect skill gaps, and get personalized learning roadmaps using AI and NLP.

## ✨ Features

- **Resume Analysis**: Parse and analyze resumes using NLP
- **Skill Gap Detection**: Identify missing skills for target roles
- **Career Role Prediction**: Suggest suitable career paths (Data Analyst, ML Engineer, Web Developer, etc.)
- **Personalized Learning Roadmap**: Generate customized learning paths
- **Interview Question Recommendations**: Get role-specific interview questions
- **Placement Readiness Score**: Assess placement preparation level
- **AI Mentor Chat**: Interactive AI-powered career mentoring
- **Dashboard**: View analytics and progress
- **Admin Panel**: Manage users and content

## 🏗️ Project Structure

```
ai-career-mentor/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── auth/
│   ├── database/
│   ├── resume_processor/
│   ├── ai_engine/
│   ├── dashboard/
│   ├── mentor_chat/
│   ├── admin/
│   └── utils/
├── tests/
├── deployment/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

- **Backend**: Flask/FastAPI
- **Database**: PostgreSQL/SQLite
- **AI/ML**: Scikit-learn, NLTK, spaCy, Pandas
- **Frontend**: Streamlit
- **NLP**: Transformers, PyPDF2
- **Deployment**: Docker, AWS/Heroku
- **Testing**: Pytest, unittest

## 📋 Prerequisites

- Python 3.8+
- pip
- PostgreSQL (optional)
- Virtual environment

## 🚀 Quick Start

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables: `cp .env.example .env`
6. Run migrations: `python manage.py migrate`
7. Start the application: `python app.py`

## 📚 Modules

### 1. Authentication
- User registration & login
- JWT token management
- Password encryption

### 2. Database Models
- User models
- Resume models
- Career recommendations
- Learning paths

### 3. Resume Upload & Parsing
- File upload handling
- PDF/DOCX parsing
- Text extraction & preprocessing

### 4. AI Recommendation Engine
- Skill extraction
- Role matching
- Learning path generation
- Interview question recommendations

### 5. Dashboard
- User progress tracking
- Skill analytics
- Career recommendations display

### 6. AI Mentor Chat
- Conversational AI
- Career guidance
- Real-time chat interface

### 7. Admin Panel
- User management
- Content management
- Analytics

### 8. Testing
- Unit tests
- Integration tests
- API tests

### 9. Deployment
- Docker configuration
- GitHub Actions CI/CD
- Production setup

## 🤝 Contributing

Contributions welcome! Please follow the contributing guidelines.

## 📝 License

MIT License

## 👨‍💻 Author

yashkunjir2006-commits

---

**Made with ❤️ for students aspiring for great careers**
