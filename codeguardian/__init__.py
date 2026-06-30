"""
CodeGuardian AI - Code Review Assistant
Made with 💜 by Vivi

Your AI pair programmer that reviews code before you commit!
"""

__version__ = "0.1.0"
__author__ = "Vivi (Bisti Ghosh)"
__description__ = "AI-powered code reviewer for your terminal"

from codeguardian.reviewer import CodeReviewer
from codeguardian.git_utils import GitHelper, is_git_repo
from codeguardian.config import ReviewConfig, load_config, save_default_config

__all__ = [
    "CodeReviewer",
    "GitHelper",
    "ReviewConfig",
    "load_config",
    "save_default_config",
    "is_git_repo"
]