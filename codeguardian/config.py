"""
Configuration for CodeGuardian
Made with 💜 by Vivi
"""

from dataclasses import dataclass
from typing import Optional
import yaml
import os


@dataclass
class ReviewConfig:
    """Configuration for code review"""
    
    focus: str = "general"  # general, security, performance
    max_tokens: int = 2000
    auto_stage: bool = False
    verbose: bool = False
    exclude_patterns: list = None
    include_patterns: list = None
    
    def __post_init__(self):
        if self.exclude_patterns is None:
            self.exclude_patterns = [
                "*.lock",
                "*.json",
                "__pycache__",
                ".git",
                "node_modules"
            ]
        
        if self.include_patterns is None:
            self.include_patterns = [
                "*.py",
                "*.js",
                "*.ts",
                "*.java",
                "*.go",
                "*.rs",
                "*.cpp",
                "*.c",
            ]


def load_config(config_path: str = ".codeguardian.yml") -> ReviewConfig:
    """Load configuration from YAML file"""
    
    if not os.path.exists(config_path):
        return ReviewConfig()
    
    try:
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)
        
        if not data:
            return ReviewConfig()
        
        return ReviewConfig(
            focus=data.get('focus', 'general'),
            max_tokens=data.get('max_tokens', 2000),
            auto_stage=data.get('auto_stage', False),
            verbose=data.get('verbose', False),
            exclude_patterns=data.get('exclude_patterns'),
            include_patterns=data.get('include_patterns')
        )
    
    except Exception as e:
        print(f"Error loading config: {e}")
        return ReviewConfig()


def save_default_config(config_path: str = ".codeguardian.yml"):
    """Save default configuration file"""
    
    default_config = {
        'focus': 'general',
        'max_tokens': 2000,
        'auto_stage': False,
        'verbose': False,
        'exclude_patterns': [
            '*.lock',
            '*.json',
            '__pycache__',
            '.git',
            'node_modules'
        ],
        'include_patterns': [
            '*.py',
            '*.js',
            '*.ts',
            '*.java',
            '*.go',
            '*.rs',
            '*.cpp',
            '*.c'
        ]
    }
    
    try:
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f, default_flow_style=False)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False