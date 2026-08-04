"""
Review screen for displaying commits.
"""

from rich.console import Console
from rich.panel import Panel

from ai_commit_labeler.models import Prediction
from ai_commit_labeler.models import Commit


class ReviewScreen:
    """
    Displays commit information in the terminal.
    """

    def __init__(self) -> None:
        self.console = Console()

    def display_review(self, commit: Commit, prediction: Prediction) -> None:
        """
        Display commit and AI prediction.
        """

        content = f"""
    [bold cyan]📦 Repository[/bold cyan]
    {commit.repository}

    [bold cyan]🔖 SHA[/bold cyan]
    {commit.sha[:7]}

    [bold cyan]💬 Commit[/bold cyan]
    {commit.commit_message}

    [bold cyan]📄 Changed Files[/bold cyan]
    {commit.changed_filenames or "—"}

    ----------------------------------------

    [bold green]🤖 AI Suggestion[/bold green]

    Label:
    {prediction.label}

    Confidence:
    {prediction.confidence}%

    Reason:
    {prediction.reason}
    """

        self.console.print(
            Panel(
                content.strip(),
                title="AI Commit Labeler",
                border_style="green",
                expand=False,
            )
        )