"""
Progress display utilities.
"""

from rich.console import Console
from rich.progress import Progress

console = Console()


class ProgressTracker:

    def __init__(self, total):
        self.total = total
        self.current = 0

        # 🔥 ADD THESE
        self.accepted = 0
        self.overridden = 0
        self.skipped = 0

    def start(self):
        print(f"Starting review of {self.total} commits...\n")

    def advance(self):
        self.current += 1

    def stop(self):
        print("\nReview stopped.")

    # 🔥 ADD THESE METHODS
    def mark_accepted(self):
        self.accepted += 1

    def mark_overridden(self):
        self.overridden += 1

    def mark_skipped(self):
        self.skipped += 1

    def show_summary(self):

        print("\n" + "=" * 40)
        print("Review Summary")
        print("=" * 40)

        total_reviewed = self.accepted + self.overridden + self.skipped

        print(f"Total Reviewed : {total_reviewed}")
        print(f"Accepted       : {self.accepted}")
        print(f"Overridden     : {self.overridden}")
        print(f"Skipped        : {self.skipped}")