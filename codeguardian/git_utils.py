"""
Git Integration for CodeGuardian
Made with 💜 by Vivi
"""

import os
from typing import List, Optional
from git import Repo, InvalidGitRepositoryError, GitCommandError
from codeguardian.components.diff_parser import parse_diff, is_significant_change


class GitHelper:
    """Helper class for Git operations"""
    
    def __init__(self, repo_path: str = "."):
        """Initialize Git helper"""
        try:
            self.repo = Repo(repo_path, search_parent_directories=True)
        except InvalidGitRepositoryError:
            raise Exception("Not a git repository! Please run this command in a git repo.")
    
    def get_staged_files(self) -> List[str]:
        """Get list of staged files"""
        try:
            staged = [item.a_path for item in self.repo.index.diff("HEAD")]
            return staged
        except GitCommandError:
            # No commits yet, get all staged files
            return [item.path for item in self.repo.index.entries.keys()]
    
    def get_unstaged_files(self) -> List[str]:
        """Get list of unstaged but modified files"""
        return [item.a_path for item in self.repo.index.diff(None)]
    
    def get_staged_diff(self) -> str:
        """Get diff of staged changes"""
        try:
            return self.repo.git.diff('--staged')
        except GitCommandError:
            # No commits yet
            return self.repo.git.diff('--cached')
    
    def get_file_diff(self, filename: str) -> str:
        """Get diff for a specific file"""
        try:
            return self.repo.git.diff('--staged', '--', filename)
        except GitCommandError:
            return self.repo.git.diff('--cached', '--', filename)
    
    def get_commit_diff(self, commit: str = "HEAD") -> str:
        """Get diff of a specific commit"""
        try:
            return self.repo.git.show(commit)
        except GitCommandError as e:
            raise Exception(f"Failed to get commit diff: {str(e)}")
    
    def get_diff_between_commits(self, commit1: str, commit2: str) -> str:
        """Get diff between two commits"""
        try:
            return self.repo.git.diff(commit1, commit2)
        except GitCommandError as e:
            raise Exception(f"Failed to get diff: {str(e)}")
    
    def is_repo_clean(self) -> bool:
        """Check if repository has uncommitted changes"""
        return not self.repo.is_dirty()
    
    def get_current_branch(self) -> str:
        """Get current branch name"""
        return self.repo.active_branch.name
    
    def get_changed_files(self, specific_files: Optional[List[str]] = None) -> List[dict]:
        """Get all changed files with their diffs"""
        
        if specific_files:
            # Review specific files
            changes = []
            for file in specific_files:
                if os.path.exists(file):
                    diff = self.get_file_diff(file)
                    if diff and is_significant_change(diff):
                        changes.extend(parse_diff(diff))
            return changes
        else:
            # Review all staged changes
            diff = self.get_staged_diff()
            if not diff:
                return []
            
            return [
                change for change in parse_diff(diff) 
                if is_significant_change(change['diff'])
            ]
    
    def stage_files(self, files: List[str]):
        """Stage files for commit"""
        self.repo.index.add(files)
    
    def get_last_commit_message(self) -> str:
        """Get last commit message"""
        try:
            return self.repo.head.commit.message
        except:
            return ""


def is_git_repo(path: str = ".") -> bool:
    """Check if directory is a git repository"""
    try:
        Repo(path, search_parent_directories=True)
        return True
    except InvalidGitRepositoryError:
        return False