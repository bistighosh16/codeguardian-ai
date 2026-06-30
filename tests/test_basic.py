"""
Basic tests for CodeGuardian
Made with 💜 by Vivi
"""

import pytest
from codeguardian.prompts import get_review_prompt, SYSTEM_PROMPT
from codeguardian.components.diff_parser import detect_language, count_changes
from codeguardian.config import ReviewConfig


class TestPrompts:
    """Test prompt generation"""
    
    def test_system_prompt_exists(self):
        """Test that system prompt is defined"""
        assert SYSTEM_PROMPT is not None
        assert "CodeGuardian" in SYSTEM_PROMPT
    
    def test_review_prompt_generation(self):
        """Test review prompt generation"""
        prompt = get_review_prompt(
            filename="test.py",
            language="python",
            diff="+ print('hello')",
            focus="general"
        )
        
        assert prompt is not None
        assert "test.py" in prompt
        assert "python" in prompt.lower()
    
    def test_security_focus_prompt(self):
        """Test security-focused prompt"""
        prompt = get_review_prompt(
            filename="auth.py",
            language="python",
            diff="+ password = request.args.get('pass')",
            focus="security"
        )
        
        assert "security" in prompt.lower()


class TestDiffParser:
    """Test diff parsing functionality"""
    
    def test_detect_python(self):
        """Test Python language detection"""
        assert detect_language("main.py") == "python"
    
    def test_detect_javascript(self):
        """Test JavaScript language detection"""
        assert detect_language("app.js") == "javascript"
    
    def test_detect_typescript(self):
        """Test TypeScript language detection"""
        assert detect_language("app.tsx") == "typescript"
    
    def test_detect_java(self):
        """Test Java language detection"""
        assert detect_language("Main.java") == "java"
    
    def test_unknown_language(self):
        """Test unknown file type"""
        assert detect_language("unknown.xyz") == "text"
    
    def test_count_changes(self):
        """Test change counting"""
        diff = """
- old line
+ new line
+ another new
"""
        additions, deletions = count_changes(diff)
        assert additions == 2
        assert deletions == 1


class TestConfig:
    """Test configuration"""
    
    def test_default_config(self):
        """Test default configuration"""
        config = ReviewConfig()
        
        assert config.focus == "general"
        assert config.max_tokens == 2000
        assert config.auto_stage == False
        assert config.verbose == False
    
    def test_custom_config(self):
        """Test custom configuration"""
        config = ReviewConfig(
            focus="security",
            max_tokens=3000,
            verbose=True
        )
        
        assert config.focus == "security"
        assert config.max_tokens == 3000
        assert config.verbose == True
    
    def test_exclude_patterns(self):
        """Test exclude patterns"""
        config = ReviewConfig()
        
        assert "*.lock" in config.exclude_patterns
        assert ".git" in config.exclude_patterns
    
    def test_include_patterns(self):
        """Test include patterns"""
        config = ReviewConfig()
        
        assert "*.py" in config.include_patterns
        assert "*.js" in config.include_patterns


if __name__ == "__main__":
    pytest.main([__file__, "-v"])