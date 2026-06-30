===START===
# CodeGuardian AI 💜🤖

Your AI pair programmer that reviews code before you commit!

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with 💜](https://img.shields.io/badge/Made%20with-💜-magenta)](https://github.com/bistighosh16/codeguardian-ai)

## What is CodeGuardian AI?

CodeGuardian AI is a terminal-based code review assistant powered by Groq's AI. It analyzes your git changes and provides intelligent, constructive feedback right in your terminal!

## Why CodeGuardian?

- 🤖 **AI-Powered** - Uses Groq's Llama 3.3 70B
- ⚡ **Lightning Fast** - Get reviews in seconds
- 🔒 **Secure** - Runs locally, never exposes code
- 🎨 **Beautiful UI** - Purple-themed terminal
- 🔧 **Flexible** - Review staged changes or commits
- 🎯 **Focused** - General, Security, or Performance reviews
- 💰 **Free** - Uses Groq's free API!

## Quick Start

### Installation
git clone https://github.com/bistighosh16/codeguardian-ai.git
cd codeguardian-ai
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -e .


### Setup

1. Get a free Groq API key at [console.groq.com](https://console.groq.com)

2. Create `.env` file with:
GROQ_API_KEY=your_api_key_here


3. Initialize:
codeguardian init


## Your First Review
Stage your changes
git add <files>

Run CodeGuardian
codeguardian review

Security-focused review
codeguardian review --focus security

Performance-focused review
codeguardian review --focus performance


## Commands

### codeguardian review

Review staged git changes with AI.
codeguardian review # Review all staged
codeguardian review main.py # Specific files
codeguardian review --focus security # Security focus
codeguardian review --verbose # Show diffs


**Options:**
- `--focus / -f` : general, security, performance
- `--commit / -c` : Review specific commit
- `--verbose / -v` : Detailed output
- `--init` : Initialize config

### codeguardian status

Show git repository status.
codeguardian status


### codeguardian version

Display version information.
codeguardian version


### codeguardian init

Initialize configuration file.
codeguardian init


## Configuration

CodeGuardian looks for `.codeguardian.yml`:
focus: general
max_tokens: 2000
auto_stage: false
verbose: false

exclude_patterns:

"*.lock"
"*.json"
"pycache"
".git"
include_patterns:

"*.py"
"*.js"
"*.ts"
"*.java"


## Features

### AI Code Review

Analyzes code using Groq's Llama 3.3 70B:
- Identifies bugs and code smells
- Provides actionable suggestions
- Rates severity: CRITICAL, HIGH, MEDIUM, LOW

### Security Review
codeguardian review --focus security


Focus on security vulnerabilities:
- SQL injection risks
- XSS vulnerabilities
- Hardcoded secrets
- Authentication issues

### Performance Review
codeguardian review --focus performance


Focus on optimizations:
- Algorithm efficiency
- Database optimization
- Memory leaks
- Resource management

### Beautiful Terminal UI

- Purple-themed interface 💜
- ASCII art banner
- Syntax-highlighted diffs
- Progress spinners
- Organized tables

### Git Integration

- Review staged changes
- Review specific files
- Review commits
- Smart diff parsing
- Language detection

## Supported Languages

Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, SQL, Bash, and more!

## Tech Stack

- **Python 3.11+** - Core language
- **Typer** - CLI framework
- **Rich** - Terminal UI
- **Groq API** - AI review
- **GitPython** - Git integration
- **PyYAML** - Configuration

## How It Works
You stage changes
↓
codeguardian review
↓
Extract git diff
↓
Send to Groq AI
↓
Get beautiful review
↓
Fix issues & commit! 🚀


## Contributing

We'd love contributions!

1. Fork the repo
2. Create feature branch
3. Make changes
4. Submit PR
git clone https://github.com/bistighosh16/codeguardian-ai.git
cd codeguardian-ai
python -m venv venv
source venv/bin/activate
pip install -e .


## License

MIT License - See LICENSE file for details.
Made with 💜 by Bisti Ghosh


## Roadmap

- [ ] Publish to PyPI
- [ ] GitHub Actions integration
- [ ] Pre-commit hook support
- [ ] VS Code extension
- [ ] Web UI dashboard
- [ ] Custom AI model support
- [ ] Team collaboration features
- [ ] CI/CD pipeline integration

## Get in Touch

- 🐙 GitHub: [@bistighosh16](https://github.com/bistighosh16)
- 💼 LinkedIn: [Bisti Ghosh](https://www.linkedin.com/in/bisti-ghosh-it-660488387/)

---

**CodeGuardian AI** - Because great code deserves a great reviewer!
╔═══════════════════════════════╗
║ Made with 💜 by Vivi ║
║ ║
║ "Code that reviews itself" ║
╚═══════════════════════════════╝


⭐ If you love CodeGuardian, star the repo!

**Happy coding! 🚀💜**
