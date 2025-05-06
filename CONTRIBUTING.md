# Contributing to HIA (Health Insights Agent)

Thank you for considering contributing to HIA! This document provides guidelines and instructions to help you get started.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
  - [Development Environment Setup](#development-environment-setup)
  - [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
  - [Branching Strategy](#branching-strategy)
  - [Commit Guidelines](#commit-guidelines)
  - [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We welcome contributions from everyone regardless of level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality.

## Getting Started

### Development Environment Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/harshhh28/hia.git
   cd hia
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   Create a `.streamlit/secrets.toml` file with the following variables:
   ```toml
   SUPABASE_URL = "your-supabase-url"
   SUPABASE_KEY = "your-supabase-key"
   GROQ_API_KEY = "your-groq-api-key"
   ```

4. **Set up Supabase database**:
   - Use the SQL script provided at `public/db/script.sql` to set up the required schema
   - Optional: Turn off email confirmation on signup in Supabase settings

5. **Run the application**:
   ```bash
   streamlit run src/main.py
   ```

### Project Structure

Familiarize yourself with the project structure:
```
hia/
├── src/
│   ├── main.py                 # Application entry point
│   ├── auth/                   # Authentication related modules
│   ├── components/             # UI Components
│   ├── config/                 # Configuration files
│   ├── services/               # Service integrations
│   ├── agents/                 # Agent-based architecture components
│   └── utils/                  # Utility functions
```

## Development Workflow

### Branching Strategy

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

2. Keep your branch updated with the main branch:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

### Commit Guidelines

- Use clear, descriptive commit messages
- Start with a verb in the present tense (e.g., "Add feature" not "Added feature")
- Reference issue numbers when applicable (e.g., "Fix #123: Update PDF validation")

### Pull Request Process

1. Ensure your code follows the coding standards
2. Update documentation if needed
3. Make sure all tests pass
4. Create a pull request with a clear title and description
5. Link any relevant issues
6. Wait for maintainers to review your PR

## Coding Standards

- Follow Python PEP 8 style guide
- Use meaningful variable and function names
- Include docstrings for functions and classes
- Keep functions focused on a single responsibility
- Organize imports alphabetically within their groups

## Testing

- Test your changes across different environments if possible

## Documentation

- Update the README.md if you add or change features
- Document functions and classes with proper docstrings
- Keep comments up-to-date with code changes

## Issue Reporting

When reporting issues, please include:

1. Description of the issue
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment details (OS, Python version, etc.)
6. Screenshots if applicable

---

Thank you for contributing to HIA! Your efforts help make this project better for everyone. 