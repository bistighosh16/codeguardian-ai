"""
AI Code Reviewer using Groq API
Made with 💜 by Vivi
"""

import os
from typing import Optional
from groq import Groq
from dotenv import load_dotenv
from codeguardian.prompts import get_review_prompt, SYSTEM_PROMPT

# Load environment variables
load_dotenv()


class CodeReviewer:
    """AI-powered code reviewer using Groq"""
    
    def __init__(self):
        """Initialize the code reviewer"""
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in .env file! "
                "Please add your API key to .env file."
            )
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
        self.system_prompt = SYSTEM_PROMPT
    
    def review_code(
        self,
        filename: str,
        diff: str,
        language: str = "python",
        focus: str = "general",
        max_tokens: int = 2000
    ) -> str:
        """
        Review code using Groq AI
        
        Args:
            filename: Name of the file being reviewed
            diff: The code diff/changes
            language: Programming language
            focus: Review focus - "general", "security", or "performance"
            max_tokens: Maximum tokens in response
        
        Returns:
            AI review text
        """
        
        # Generate the prompt
        user_prompt = get_review_prompt(
            filename=filename,
            language=language,
            diff=diff,
            focus=focus
        )
        
        try:
            # Call Groq API
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
            
            return message.content[0].text
        
        except Exception as e:
            return f"Error during review: {str(e)}"
    
    def review_multiple_files(
        self,
        files: list,
        focus: str = "general"
    ) -> dict:
        """
        Review multiple files
        
        Args:
            files: List of dicts with 'file', 'diff', 'language' keys
            focus: Review focus area
        
        Returns:
            Dictionary with review results
        """
        
        results = {}
        
        for file_info in files:
            filename = file_info.get('file', 'unknown')
            diff = file_info.get('diff', '')
            language = file_info.get('language', 'text')
            
            review = self.review_code(
                filename=filename,
                diff=diff,
                language=language,
                focus=focus
            )
            
            results[filename] = {
                'review': review,
                'language': language,
                'focus': focus
            }
        
        return results
    
    def get_quick_summary(self, review_text: str, filename: str) -> str:
        """
        Get a quick 1-line summary of the review
        
        Args:
            review_text: Full review text
            filename: Name of file
        
        Returns:
            Quick summary
        """
        
        prompt = f"""Given this code review:

{review_text}

Provide a single-line summary (max 100 chars) for file '{filename}'. 
Start with emoji and keep it brief."""
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=100,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            return message.content[0].text.strip()
        
        except Exception as e:
            return f"⚠️ Could not generate summary: {str(e)}"
    
    def extract_severity_levels(self, review_text: str) -> dict:
        """
        Extract severity levels from review
        
        Returns dict with counts of each severity
        """
        
        severities = {
            'CRITICAL': review_text.count('CRITICAL'),
            'HIGH': review_text.count('HIGH'),
            'MEDIUM': review_text.count('MEDIUM'),
            'LOW': review_text.count('LOW')
        }
        
        return severities