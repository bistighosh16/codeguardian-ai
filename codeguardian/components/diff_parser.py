"""
Diff Parser for CodeGuardian
Made with 💜 by Vivi
"""

import re
from typing import Dict, List, Tuple


def parse_diff(diff_text: str) -> List[Dict[str, any]]:
    """Parse git diff into structured format"""
    
    changes = []
    current_file = None
    current_diff = []
    
    lines = diff_text.split('\n')
    
    for line in lines:
        # New file detected
        if line.startswith('diff --git'):
            if current_file:
                changes.append({
                    'file': current_file,
                    'diff': '\n'.join(current_diff),
                    'language': detect_language(current_file)
                })
            
            # Extract filename
            match = re.search(r'b/(.+)$', line)
            if match:
                current_file = match.group(1)
                current_diff = []
        
        elif current_file:
            current_diff.append(line)
    
    # Add last file
    if current_file:
        changes.append({
            'file': current_file,
            'diff': '\n'.join(current_diff),
            'language': detect_language(current_file)
        })
    
    return changes


def detect_language(filename: str) -> str:
    """Detect programming language from file extension"""
    
    extensions = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.java': 'java',
        '.cpp': 'cpp',
        '.c': 'c',
        '.h': 'c',
        '.cs': 'csharp',
        '.go': 'go',
        '.rs': 'rust',
        '.php': 'php',
        '.rb': 'ruby',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.scala': 'scala',
        '.r': 'r',
        '.sql': 'sql',
        '.sh': 'bash',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.json': 'json',
        '.xml': 'xml',
        '.html': 'html',
        '.css': 'css',
        '.scss': 'scss',
        '.md': 'markdown',
    }
    
    for ext, lang in extensions.items():
        if filename.endswith(ext):
            return lang
    
    return 'text'


def count_changes(diff_text: str) -> Tuple[int, int]:
    """Count additions and deletions in diff"""
    
    additions = 0
    deletions = 0
    
    for line in diff_text.split('\n'):
        if line.startswith('+') and not line.startswith('+++'):
            additions += 1
        elif line.startswith('-') and not line.startswith('---'):
            deletions += 1
    
    return additions, deletions


def extract_changed_lines(diff_text: str) -> List[str]:
    """Extract only the changed lines from diff"""
    
    changed_lines = []
    
    for line in diff_text.split('\n'):
        if line.startswith('+') or line.startswith('-'):
            if not (line.startswith('+++') or line.startswith('---')):
                changed_lines.append(line)
    
    return changed_lines


def is_significant_change(diff_text: str) -> bool:
    """Check if the change is significant enough to review"""
    
    # Skip if only whitespace changes
    changed_lines = extract_changed_lines(diff_text)
    
    if not changed_lines:
        return False
    
    # Check if all changes are just whitespace
    non_whitespace = [line for line in changed_lines if line.strip() not in ['+', '-']]
    
    return len(non_whitespace) > 0


def get_context_lines(diff_text: str, context: int = 3) -> str:
    """Get diff with more context lines"""
    # This is a simplified version
    # In production, you'd parse the diff chunks properly
    return diff_text