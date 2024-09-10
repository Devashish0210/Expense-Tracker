import argparse
from commands.add import add_expense
from commands.delete import delete_exp
from commands.list import list_expenses
from commands.summary import show_summary

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command", help="sub-commands")

# Parser for add
parser_add = subparsers.add_parser("add", help="Add a new expense")
parser_add.add_argument('--category', type=str, required=True, help="Category of the expense")
parser_add.add_argument('--description', type=str, required=True, help="Description of the expense")
parser_add.add_argument('--amount', type=float, required=True, help="Amount of the expense")

# Parser for list
parser_list = subparsers.add_parser("list", help="List all expenses")

# Parser for delete
parser_delete = subparsers.add_parser("delete", help="Delete an expense by id")
parser_delete.add_argument('--id', type=int, required=True, help="ID of the expense")

# Parser for summary
parser_summary = subparsers.add_parser("summary", help="Summary of expenses for a certain month")
parser_summary.add_argument('--month', type=int, choices= range(1,13), required=True, help="Month (1-12) of the expense")

args = parser.parse_args()

match args.command:
    case 'add':
        add_expense(args.category, args.description, args.amount)
    case 'list':
        list_expenses()
    case 'delete':
        delete_exp(args.id)
    case 'summary':
        show_summary(args.month)
    case _:
        parser.print_help()