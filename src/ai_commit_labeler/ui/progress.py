import sys


class ProgressTracker:

    def __init__(self, total):
        self.total = total
        self.current = 0

        # stats
        self.accepted = 0
        self.overridden = 0
        self.skipped = 0

    def start(self):
        self._print_progress()

    def advance(self):
        self.current += 1
        self._print_progress()

    def stop(self):
        print()

    # ✅ NEW METHODS
    def mark_accepted(self):
        self.accepted += 1

    def mark_overridden(self):
        self.overridden += 1

    def mark_skipped(self):
        self.skipped += 1

    def show_summary(self):

        print("\n\n========== Review Summary ==========")
        print(f"Total Reviewed : {self.current}")
        print(f"Accepted       : {self.accepted}")
        print(f"Overridden     : {self.overridden}")
        print(f"Skipped        : {self.skipped}")

        if self.current > 0:
            accuracy = (self.correct_predictions / self.current) * 100
            override_rate = (self.overridden / self.current) * 100
        else:
            accuracy = 0
            override_rate = 0

        print("\n---------- AI Performance ----------")
        print(f"AI Accuracy    : {accuracy:.2f}%")
        print(f"Override Rate  : {override_rate:.2f}%")

        print("====================================")

    def _print_progress(self):
        percent = int((self.current / self.total) * 100)
        bar_length = 30
        filled_length = int(bar_length * self.current // self.total)

        bar = "█" * filled_length + "-" * (bar_length - filled_length)

        sys.stdout.write(
            f"\rProgress: |{bar}| {percent}% ({self.current}/{self.total})"
        )
        sys.stdout.flush()