"""
Interactive terminal prompts.
"""

from rich.console import Console

console = Console()


def ask_user_choice() -> str:
    """
    Ask the reviewer what to do.
    """

    console.print()
    console.print("[bold green][A][/bold green] Accept AI label")
    console.print("[bold yellow][O][/bold yellow] Override label")
    console.print("[bold blue][S][/bold blue] Skip")
    console.print("[bold red][Q][/bold red] Quit")
    console.print()

    return input("Choice: ").strip().upper()


def ask_override_label() -> str:
    """
    Ask the reviewer to choose a new label.
    """

    console.print()
    console.print("[bold cyan]Available Labels[/bold cyan]")
    console.print("1. LOW_VALUE")
    console.print("2. USEFUL")
    console.print("3. UNCERTAIN")
    console.print()

    while True:

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            return "LOW_VALUE"

        elif choice == "2":
            return "USEFUL"

        elif choice == "3":
            return "UNCERTAIN"

        console.print("[red]Invalid choice. Try again.[/red]")