from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

console = Console()
first_name = Prompt.ask("Введіть ім'я")
last_name = Prompt.ask("Введіть прізвище")
group = Prompt.ask("Введіть групу", choices=["КБ-101", "КБ-102", "КБ-103"],case_sensitive=False)
variant = IntPrompt.ask("Введіть варіант")

first_name = Text(first_name, style="bold red")
last_name = Text(last_name, style="bold #008700")
group = Text(group, style="bold #5fd7ff")
variant = Text(f"{variant}", style="italic #d70087")
text = Text("Інформація про студента", style="bold bright_red")

table = Table(title=text, header_style="bold bright_green")
table.add_column("Ім'я ", style="bold red", justify="center", no_wrap=True)
table.add_column("Прізвище ", style="bold #008700", justify="center")
table.add_column("Група", style="bold #5fd7ff", justify="center")
table.add_column("Варіант", style="italic #d70087", justify="center")

table.add_row(first_name, last_name, group, f"{variant}")
console.print(table, justify="center")

console.print(first_name, last_name, group, variant, sep='\n')
