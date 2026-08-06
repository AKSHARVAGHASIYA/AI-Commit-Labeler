"""
Progress display utilities.
"""

from rich.console import Console
from rich.progress import Progress

console = Console()


class ProgressTracker:
    def __init__(self, total: int):
        self.progress = Progress()
        self.task = self.progress.add_task(
            "[green]Review Progress",
            total=total
        )

    def start(self):
        self.progress.start()

    def advance(self):
        self.progress.advance(self.task)

    def stop(self):
        self.progress.stop()