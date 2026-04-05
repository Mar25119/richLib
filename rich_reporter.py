# rich_reporter.py

import platform
import sys
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.syntax import Syntax

def main():
    console = Console()

    # Заголовок
    console.print(Panel.fit("[bold blue]Системный отчёт[/bold blue]", border_style="blue"))

    # Таблица с информацией
    table = Table(title="Информация о системе", style="cyan")
    table.add_column("Параметр", style="magenta")
    table.add_column("Значение", style="green")

    table.add_row("Операционная система", platform.system())
    table.add_row("Версия ОС", platform.version())
    table.add_row("Архитектура", platform.machine())
    table.add_row("Python", sys.version)
    table.add_row("Платформа", platform.platform())

    console.print(table)

    # Имитация загрузки
    console.print("\n[bold yellow]Имитация загрузки данных...[/bold yellow]")
    with Progress() as progress:
        task = progress.add_task("[green]Загрузка...", total=100)
        while not progress.finished:
            progress.update(task, advance=5)
            time.sleep(0.05)

    # Итоговая панель
    console.print("\n", Panel("[bold green]Отчёт успешно сгенерирован![/bold green]", border_style="green"))

    # Пример кода с подсветкой
    code_example = '''from rich.console import Console
console = Console()
console.print("Привет, Rich!", style="bold red")'''

    console.print("\n[bold]Пример использования:[/bold]")
    syntax = Syntax(code_example, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

if __name__ == "__main__":
    main()