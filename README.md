# 🩺 HIA (Health Insights Agent)

AI Agent to analyze blood reports and provide detailed health insights.

<p align="center">
  <a href="https://github.com/TechFreak2003/hia/issues"><img src="https://img.shields.io/github/issues/TechFreak2003/hia"></a> 
  <a href="https://github.com/TechFreak2003/hia/stargazers"><img src="https://img.shields.io/github/stars/TechFreak2003/hia"></a>
  <a href="https://github.com/TechFreak2003/hia/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  </a>
</p>

<p align="center">
  <a href="#-features">Features</a> |
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> |
  <a href="#-installation">Installation</a> |
  <a href="#-contributing">Contributing</a> |
  <a href="#%EF%B8%8F-author">Author</a>
</p>

<p align="center">
  <a href="https://github.com/TechFreak2003/hia"><img src="https://raw.githubusercontent.com/TechFreak2003/hia/main/public/HIA_demo.gif" alt="Usage Demo"></a>
</p>

## 🌟 Features

- Intelligent agent-based architecture with multi-model cascade system
- In-context learning from previous analyses and knowledge base building
- Medical report analysis with personalized health insights
- PDF upload, validation and text extraction (up to 20MB)
- Secure user authentication and session management
- Session history with report analysis tracking
- Modern, responsive UI with real-time feedback

## 🛠️ Tech Stack

- **Frontend Framework**: Streamlit
- **AI Integration**: Multi-model architecture via Groq
  - Primary: LLaMA-3.3-70B-Versatile
  - Secondary: LLaMA-3-8B-8192
  - Tertiary: Mixtral-8x7B-32768
  - Fallback: Gemma-7B-IT
- **Database**: Supabase
- **PDF Processing**: PDFPlumber
- **Authentication**: Supabase Auth

## 🚀 Installation

#### Requirements 📋

- Python 3.8+
- Streamlit 1.30.0+
- Supabase account
- Groq API key
- PDFPlumber
- Python-magic-bin (Windows) or Python-magic (Linux/Mac)

#### Getting Started 📝

1. Clone the repository:

```bash
git clone https://github.com/TechFreak2003/hia.git
cd hia
