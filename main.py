import datetime

from rich import print
from rich.console import Console

from application.salary import calculate_salary
from application.db.people import get_employees

console = Console(force_terminal=True)

if __name__ == '__main__':
    current_date = datetime.date.today()

    console.rule("[bold green]Бухгалтерия[/bold green]")
    console.print(f"[cyan]Дата запуска программы:[/cyan] [bold]{current_date}[/bold]")
    console.rule()

    console.print("\n[bold yellow]Сотрудники:[/bold yellow]")
    get_employees()

    console.print("\n[bold yellow]Расчёт зарплаты:[/bold yellow]")
    calculate_salary()

    console.rule("[bold green]Программа завершена[/bold green]")