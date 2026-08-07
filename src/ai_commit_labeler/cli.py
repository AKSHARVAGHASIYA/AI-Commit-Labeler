"""
Command Line Interface for AI Commit Labeler.
"""

import typer

from ai_commit_labeler.services import ReviewService
from ai_commit_labeler.ui import (
    ReviewScreen,
    ask_user_choice,
    ask_override_label,
    ProgressTracker,
)
from ai_commit_labeler.version import __version__
from ai_commit_labeler.storage.csv_writer import CSVWriter

app = typer.Typer(add_completion=False)

review_service = ReviewService()
screen = ReviewScreen()


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

    tracker = ProgressTracker(len(commits))
    tracker.start()

    writer = CSVWriter()

    typer.echo(f"\nLoaded {len(commits)} commits.\n")

    for index, commit in enumerate(commits, start=1):

        prediction = review_service.review_commit(commit)

        screen.display_review(commit, prediction)

        choice = ask_user_choice()

        if choice == "A":

            writer.save(
                commit=commit,
                prediction=prediction,
                action="accepted",
                final_label=prediction.label,
            )

            tracker.mark_accepted()
            tracker.advance()

            typer.secho("✓ Accepted\n", fg=typer.colors.GREEN)

        elif choice == "O":

            new_label = ask_override_label()

            writer.save(
                commit=commit,
                prediction=prediction,
                action="overridden",
                final_label=new_label,
            )

            tracker.mark_overridden()
            tracker.advance()

            typer.secho(
                f"✓ Saved as {new_label}\n",
                fg=typer.colors.CYAN,
            )

        elif choice == "S":

            writer.save(
                commit=commit,
                prediction=prediction,
                action="skipped",
                final_label=prediction.label,
            )

            tracker.mark_skipped()
            tracker.advance()

            typer.secho("✓ Skipped\n", fg=typer.colors.YELLOW)

        elif choice == "Q":

            tracker.stop()
            tracker.show_summary() 

            typer.secho("Exiting review session...", fg=typer.colors.RED)
            break

        else:
            typer.secho(
                "Invalid choice. Please select A, O, S, or Q.",
                fg=typer.colors.RED,
            )