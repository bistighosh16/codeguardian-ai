"""
CLI Interface for CodeGuardian
Made with 💜 by Vivi
"""

import typer
from typing import Optional, List
from pathlib import Path
from codeguardian.components.ui import (
    print_banner,
    print_success,
    print_error,
    print_info,
    print_warning,
    print_purple,
    create_review_panel,
    create_file_table,
    display_diff,
    show_progress,
    display_review_result,
    print_summary,
    ask_confirmation,
    print_divider
)
from codeguardian.reviewer import CodeReviewer
from codeguardian.git_utils import GitHelper, is_git_repo
from codeguardian.config import load_config, save_default_config

app = typer.Typer(help="CodeGuardian AI - Your AI Code Reviewer 💜")


@app.command()
def review(
    files: Optional[List[str]] = typer.Argument(None, help="Specific files to review"),
    focus: str = typer.Option(
        "general",
        "--focus",
        "-f",
        help="Review focus: general, security, performance"
    ),
    commit: Optional[str] = typer.Option(
        None,
        "--commit",
        "-c",
        help="Review specific commit (e.g., HEAD~1)"
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show verbose output"
    ),
    init_config: bool = typer.Option(
        False,
        "--init",
        help="Initialize .codeguardian.yml config file"
    )
):
    """
    Review code changes with AI
    
    Examples:
    
    \b
    # Review staged changes
    codeguardian review
    
    \b
    # Review specific files
    codeguardian review main.py utils.py
    
    \b
    # Security-focused review
    codeguardian review --focus security
    
    \b
    # Review last commit
    codeguardian review --commit HEAD
    """
    
    # Show banner
    print_banner()
    
    # Initialize config if requested
    if init_config:
        if save_default_config():
            print_success("Created .codeguardian.yml config file!")
            return
        else:
            print_error("Failed to create config file")
            return
    
    # Load configuration
    config = load_config()
    
    # Override focus if provided
    if focus != "general":
        config.focus = focus
    
    if verbose:
        config.verbose = True
    
    # Check if in git repo
    if not is_git_repo():
        print_error("Not a git repository! Please run this in a git repo.")
        raise typer.Exit(code=1)
    
    try:
        # Initialize Git helper
        git = GitHelper()
        print_success(f"Git repository detected (branch: {git.get_current_branch()})")
        print_divider()
        
        # Get changed files
        print_info("Analyzing code changes...")
        
        changed_files = git.get_changed_files(files)
        
        if not changed_files:
            print_warning("No staged changes to review!")
            print_info("Stage your changes with: git add <files>")
            return
        
        # Show files to review
        print_success(f"Found {len(changed_files)} file(s) to review")
        file_list = [f['file'] for f in changed_files]
        create_file_table(file_list)
        
        # Ask for confirmation
        if not ask_confirmation("Proceed with review?"):
            print_warning("Review cancelled!")
            return
        
        print_divider()
        
        # Initialize AI reviewer
        print_info("Initializing CodeGuardian AI...")
        reviewer = CodeReviewer()
        print_success("AI Ready! 🤖")
        print_divider()
        
        # Review each file
        total_issues = 0
        
        with show_progress(f"Reviewing {len(changed_files)} file(s)...") as progress:
            task_id = progress.add_task("", total=len(changed_files))
            
            for file_info in changed_files:
                filename = file_info['file']
                diff = file_info['diff']
                language = file_info['language']
                
                if verbose:
                    display_diff(filename, diff, language)
                
                # Review with AI
                review_result = reviewer.review_code(
                    filename=filename,
                    diff=diff,
                    language=language,
                    focus=config.focus,
                    max_tokens=config.max_tokens
                )
                
                # Display review
                display_review_result(filename, review_result)
                
                # Count issues
                severities = reviewer.extract_severity_levels(review_result)
                file_issues = sum(severities.values())
                total_issues += file_issues
                
                if verbose:
                    print_info(f"Severity breakdown: {severities}")
                
                progress.update(task_id, advance=1)
        
        print_divider()
        
        # Summary
        print_summary(len(changed_files), total_issues)
        
        if total_issues == 0:
            print_success("No major issues found! Your code looks great! 🎉")
        elif total_issues <= 3:
            print_warning(f"Found {total_issues} issue(s) to address")
        else:
            print_error(f"Found {total_issues} issue(s) - please review!")
        
        print_purple("Made with 💜 by CodeGuardian AI")
    
    except Exception as e:
        print_error(f"Error during review: {str(e)}")
        if verbose:
            import traceback
            traceback.print_exc()
        raise typer.Exit(code=1)


@app.command()
def status():
    """Show git repository status"""
    
    print_banner()
    
    if not is_git_repo():
        print_error("Not a git repository!")
        raise typer.Exit(code=1)
    
    try:
        git = GitHelper()
        
        print_info(f"Current branch: {git.get_current_branch()}")
        
        # Staged files
        staged = git.get_staged_files()
        if staged:
            print_success(f"\nStaged files ({len(staged)}):")
            for file in staged:
                print(f"  ✓ {file}")
        else:
            print_warning("\nNo staged files")
        
        # Unstaged files
        unstaged = git.get_unstaged_files()
        if unstaged:
            print_warning(f"\nUnstaged files ({len(unstaged)}):")
            for file in unstaged:
                print(f"  ✗ {file}")
        else:
            print_success("\nNo unstaged changes")
        
        print_purple("\nMade with 💜 by CodeGuardian AI")
    
    except Exception as e:
        print_error(f"Error: {str(e)}")
        raise typer.Exit(code=1)


@app.command()
def version():
    """Show version information"""
    
    print_banner()
    
    import codeguardian
    
    version_info = f"""
Version: {codeguardian.__version__}
Author: {codeguardian.__author__}
Description: {codeguardian.__description__}

Made with 💜 by Vivi
    """
    
    print_purple(version_info)


@app.command()
def init():
    """Initialize CodeGuardian in current directory"""
    
    print_banner()
    
    if not is_git_repo():
        print_error("Not a git repository!")
        raise typer.Exit(code=1)
    
    if save_default_config():
        print_success("✅ CodeGuardian initialized!")
        print_info("Config saved to: .codeguardian.yml")
        print_info("Run 'codeguardian review' to start reviewing code!")
    else:
        print_error("Failed to initialize CodeGuardian")
        raise typer.Exit(code=1)


def main():
    """Main entry point"""
    app()


if __name__ == "__main__":
    main()