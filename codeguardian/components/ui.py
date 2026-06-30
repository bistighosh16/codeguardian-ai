"""
Beautiful Terminal UI Components
Made with 💜 by Vivi
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich import box
from rich.theme import Theme

# Custom Purple Theme 💜
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "red bold",
    "success": "green bold",
    "purple": "magenta bold",
    "highlight": "bold magenta"
})

console = Console(theme=custom_theme)


def print_banner():
    """Display CodeGuardian banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║   ██████╗ ██████╗ ██████╗ ███████╗                  ║
    ║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝                  ║
    ║  ██║     ██║   ██║██║  ██║█████╗                    ║
    ║  ██║     ██║   ██║██║  ██║██╔══╝                    ║
    ║  ╚██████╗╚██████╔╝██████╔╝███████╗                  ║
    ║   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝                  ║
    ║                                                       ║
    ║   ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗          ║
    ║  ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗         ║
    ║  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║         ║
    ║  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║         ║
    ║  ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝         ║
    ║   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝          ║
    ║                                                       ║
    ║         AI-Powered Code Review Assistant              ║
    ║              Made with 💜 by Vivi                     ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """
    console.print(banner, style="bold magenta")
    console.print()


def print_success(message: str):
    """Print success message"""
    console.print(f"✅ {message}", style="success")


def print_error(message: str):
    """Print error message"""
    console.print(f"❌ {message}", style="error")


def print_warning(message: str):
    """Print warning message"""
    console.print(f"⚠️  {message}", style="warning")


def print_info(message: str):
    """Print info message"""
    console.print(f"ℹ️  {message}", style="info")


def print_purple(message: str):
    """Print in purple theme 💜"""
    console.print(message, style="purple")


def create_review_panel(title: str, content: str, severity: str = "info"):
    """Create a beautiful panel for review results"""
    
    # Color based on severity
    border_colors = {
        "CRITICAL": "red",
        "HIGH": "red",
        "MEDIUM": "yellow",
        "LOW": "cyan",
        "info": "magenta"
    }
    
    border_color = border_colors.get(severity, "magenta")
    
    panel = Panel(
        content,
        title=f"[bold]{title}[/bold]",
        border_style=border_color,
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print(panel)


def create_file_table(files: list):
    """Create a table of files being reviewed"""
    table = Table(
        title="📁 Files to Review",
        box=box.ROUNDED,
        border_style="magenta",
        show_header=True,
        header_style="bold magenta"
    )
    
    table.add_column("No.", style="cyan", width=6)
    table.add_column("File Path", style="white")
    table.add_column("Status", style="green")
    
    for idx, file in enumerate(files, 1):
        table.add_row(str(idx), file, "✓ Ready")
    
    console.print(table)
    console.print()


def display_diff(filename: str, diff_content: str, language: str = "diff"):
    """Display code diff with syntax highlighting"""
    console.print(f"\n[bold magenta]📄 {filename}[/bold magenta]\n")
    
    syntax = Syntax(
        diff_content,
        language,
        theme="monokai",
        line_numbers=True,
        word_wrap=True
    )
    
    console.print(syntax)
    console.print()


def show_progress(message: str):
    """Show a progress spinner"""
    return Progress(
        SpinnerColumn(style="magenta"),
        TextColumn("[bold magenta]{task.description}"),
        console=console,
        transient=True
    )


def display_review_result(filename: str, review_text: str):
    """Display AI review result beautifully"""
    console.print(f"\n[bold magenta]🤖 AI Review for: {filename}[/bold magenta]\n")
    
    # Render markdown for better formatting
    md = Markdown(review_text)
    
    panel = Panel(
        md,
        title="[bold]💜 CodeGuardian Review[/bold]",
        border_style="magenta",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()


def print_summary(total_files: int, total_issues: int):
    """Print review summary"""
    summary = Table(
        title="📊 Review Summary",
        box=box.ROUNDED,
        border_style="magenta",
        show_header=False
    )
    
    summary.add_column("Metric", style="bold cyan")
    summary.add_column("Value", style="bold white")
    
    summary.add_row("Files Reviewed", str(total_files))
    summary.add_row("Total Issues Found", str(total_issues))
    summary.add_row("Status", "✅ Complete" if total_issues == 0 else "⚠️ Review Required")
    
    console.print()
    console.print(summary)
    console.print("\n[bold magenta]Made with 💜 by CodeGuardian AI[/bold magenta]\n")


def ask_confirmation(question: str) -> bool:
    """Ask user for confirmation"""
    from rich.prompt import Confirm
    return Confirm.ask(f"[bold magenta]{question}[/bold magenta]")


def print_divider():
    """Print a purple divider"""
    console.print("━" * 60, style="magenta")