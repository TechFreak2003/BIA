
# 🩺 BIA (Blood Report Insights Agent)

AI Agent will analyze blood reports and provide detailed health insights.

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
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Required environment variables (in `.streamlit/secrets.toml`):

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
GROQ_API_KEY = "your-groq-api-key"
```

4. Set up Supabase database schema:

The application requires the following tables in your Supabase database:

![database schema](https://github.com/TechFreak2003/BIA/blob/main/public/db/schema.png)

You can use the SQL script provided at `public/db/script.sql` <a href="https://github.com/TechFreak2003/BIA/blob/main/public/db/script.sql">[link]</a> to set up the required database schema.

(PS: You can turn off the email confirmation on signup in Supabase settings -> signup -> email)

5. Run the application:

```bash
streamlit run src\main.py
```

## 📁 Project Structure

```
hia/
├── requirements.txt
├── README.md
├── src/
│   ├── main.py                 # Application entry point
│   ├── auth/                   # Authentication related modules
│   │   ├── auth_service.py     # Supabase auth integration
│   │   └── session_manager.py  # Session management
│   ├── components/             # UI Components
│   │   ├── analysis_form.py    # Report analysis form
│   │   ├── auth_pages.py       # Login/Signup pages
│   │   ├── footer.py           # Footer component
│   │   └── sidebar.py          # Sidebar navigation
│   ├── config/                 # Configuration files
│   │   ├── app_config.py       # App settings
│   │   └── prompts.py          # AI prompts
│   ├── services/               # Service integrations
│   │   └── ai_service.py       # AI service integration
│   ├── agents/                 # Agent-based architecture components
│   │   ├── agent_manager.py    # Agent management
│   │   └── model_fallback.py   # Model fallback logic
│   └── utils/                  # Utility functions
│       ├── validators.py       # Input validation
│       └── pdf_extractor.py    # PDF processing
```

## 👥 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, the development workflow, coding standards, and more.

We appreciate all contributions, from reporting bugs and improving documentation to implementing new features.

## 👨‍💻 Contributors

Thanks to all the amazing contributors who have helped improve this project!

| Avatar | Name | GitHub | Role | Contributions |
|--------|------|--------|------|---------------|
| <img src="https://github.com/TechFreak2003.png" width="50px" height="50px" alt="TechFreak2003"/> | Suvrodeep Das | [TechFreak2003](https://github.com/TechFreak2003) | Project Creator & Maintainer | Core implementation, Documentation |

<!-- To future contributors: Your profile will be added here when your PR is merged! -->

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Author

Created by [Suvrodeep Das](https://suvrodeepdas.dev)
