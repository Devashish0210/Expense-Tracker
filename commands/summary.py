from.utils import read_expenses, get_month
from datetime import datetime
from rich.console import Console
from rich import print

def show_summary(month=None):
    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[/bold red]")
        return
    
    month_text = ""
    if month:
        expenses = [expense for expense in expenses if datetime.fromisoformat(expense['date']).month == month]
        month_text = f" for {get_month(month)}"
    
    total_amt = sum(expense['amount'] for expense in expenses)
    console = Console()
    console.print(f"[bold]Expense Summary{month_text}[/bold]")
    console.print(f"Total Amount: [bold green]{total_amt:.2f}[/bold green]")