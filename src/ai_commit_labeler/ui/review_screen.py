"""
Review screen for displaying commits.
"""

from rich.console import Console
from rich.panel import Panel

from ai_commit_labeler.models import Commit


class ReviewScreen:
    """
    Displays commit information in the terminal.
    """

    def __init__(self) -> None:
        self.console = Console()

    def display_commit(self, commit: Commit) -> None:
        """
        Display a single commit.
        """

        content = f"""
[bold cyan]Repository[/bold cyan]
{commit.repository}

[bold cyan]SHA[/bold cyan]
{commit.sha}

[bold cyan]Commit Message[/bold cyan]
{commit.commit_message}

[bold cyan]Changed Files[/bold cyan]
{commit.changed_filenames or "N/A"}

[bold cyan]File Summary[/bold cyan]
{commit.file_summary or "N/A"}

[bold cyan]Patch Summary[/bold cyan]
{commit.patch_summary or "N/A"}
"""

        self.console.print(
            Panel(
                content.strip(),
                title="🤖 AI Commit Labeler",
                border_style="green",
                expand=False
            )
        )
        