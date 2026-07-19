"""
Command Line Interface for AI Commit Labeler.
"""

import typer

from .version import __version__

app = typer.Typer(
    help="AI-assisted GitHub Commit Annotation Tool",
    add_completion=False,
)


@app.command("version")
def version_command() -> None:
    """Show application version."""
    typer.echo(f"AI Commit Labeler v{__version__}")


@app.command("review")
def review_command() -> None:
    """Review commits."""
    typer.echo("Review command coming soon...")