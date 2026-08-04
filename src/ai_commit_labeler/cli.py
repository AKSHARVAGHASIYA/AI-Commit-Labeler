"""
Command Line Interface for AI Commit Labeler.
"""

import typer

from ai_commit_labeler.services import ReviewService
from ai_commit_labeler.storage import CSVWriter
from ai_commit_labeler.ui import ReviewScreen, ask_user_choice
from ai_commit_labeler.version import __version__

app = typer.Typer(add_completion=False)

review_service = ReviewService()
screen = ReviewScreen()
writer = CSVWriter()


@app.command()
def version():
    """Show application version."""
    typer.echo(f"AI Commit Labeler v{__version__}")


@app.command()
def review(csv_file: str):
    """
    Review commits from a CSV file.
    """

    commits = review_service.load_commits(csv_file)

    typer.echo(f"\nLoaded {len(commits)} commits.\n")

    for index, commit in enumerate(commits, start=1):

        prediction = review_service.review_commit(commit)

        screen.display_review(commit, prediction)

        choice = ask_user_choice()

        if choice == "A":

            writer.save(
                commit=commit,
                prediction=prediction,
                final_label=prediction.label,
                decision="ACCEPT",
            )

            typer.secho("✓ Accepted\n", fg=typer.colors.GREEN)

        elif choice == "S":

            writer.save(
                commit=commit,
                prediction=prediction,
                final_label=prediction.label,
                decision="SKIP",
            )

            typer.secho("✓ Skipped\n", fg=typer.colors.YELLOW)

        elif choice == "Q":

            typer.secho("Exiting review session...", fg=typer.colors.RED)
            break

        else:
            typer.secho(
                "Invalid choice. Please select A, S, or Q.",
                fg=typer.colors.RED,
            )