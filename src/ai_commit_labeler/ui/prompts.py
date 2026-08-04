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