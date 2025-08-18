import click
import os
import difflib
from utils import get_challenges, get_readme, run_solution, get_solution_diff
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich import box

@click.group()
def cli():
    """Challenge Toolkit CLI."""
    pass


@cli.command()
def list() -> None:
    """List all available challenges."""
    console = Console()
    challenges = get_challenges()
    if not challenges:
        console.print(Panel("No challenges available.", style="bold red", title="[bold red]Error[/bold red]", expand=False))
        return

    table = Table(box=box.ROUNDED, show_lines=True, expand=False, highlight=True)
    table.add_column("#", style="bold cyan", justify="center", width=4)
    table.add_column("Challenge Name", style="bold magenta", justify="left")
    for idx, challenge_name in enumerate(challenges, 1):
        table.add_row(f"[bold blue]{idx}[/bold blue]", f"[yellow]{challenge_name}[/yellow]")

    panel = Panel(
        table,
        title="🚀 [bold green]Challenges available[/bold green]",
        subtitle="Use '[bold]toolkit.py show <nombre>[/bold]' to see the instructions for a specific challenge.",
        border_style="green",
        expand=False
    )
    console.print(panel)


@cli.command()
@click.argument("name", type=click.Choice(get_challenges()))
def show(name):
    """Show the instructions for a specific challenge."""
    console = Console()
    content = get_readme(name)

    if content:
        md = Markdown(content, code_theme="monokai", inline_code_lexer="python")
        panel = Panel(
            md,
            title=f"📄 [bold magenta]Instructions for {name}[/bold magenta]",
            border_style="magenta",
            expand=False
        )
        console.print(panel)
    else:
        console.print(Panel(f"README.md for challenge '{name}' not found.", style="bold red", title="[bold red]Error[/bold red]", expand=False))

@cli.command()
@click.argument("name", type=click.Choice(get_challenges()))
def test(name):
    """Execute pytest for a challenge."""
    console = Console()
    output, exit_code = run_solution(name)
    if exit_code == 0:
        panel = Panel(
            output or "[bold green]Test passed! No output.[/bold green]",
            title=f"🛠️ [bold green]Test Output: {name}[/bold green]",
            border_style="green",
            expand=False
        )
    else:
        panel = Panel(
            output or "[bold red]Test failed! No output.[/bold red]",
            title=f"❌ [bold red]Test Failed: {name}[/bold red]",
            border_style="red",
            expand=False
        )
    console.print(panel)

@cli.command()
@click.argument("name", type=click.Choice(get_challenges()))
def diff(name):
    """Show unified diff between candidate solution and reference answer (if available)."""
    console = Console()
    output, code = get_solution_diff(name)
    style = "green" if code == 0 else ("yellow" if code == 1 else "red")
    title = f"Diff: {name}"
    console.print(Panel(output, style=style, title=title))

@cli.command(name="test_all")
def test_all():
    """Run tests for all challenges and summarize results."""
    console = Console()
    challenges = get_challenges()
    success = 0
    failure = 0
    details = []
    for ch in challenges:
        out, code = run_solution(ch)
        if code == 0:
            success += 1
            details.append(f"[green]{ch}: PASS[/green]")
        else:
            failure += 1
            details.append(f"[red]{ch}: FAIL[/red]\n[out]\n{out}")
    summary = f"Passed: {success} | Failed: {failure} | Total: {len(challenges)}\n" + "\n".join(details)
    style = "green" if failure == 0 else "red"
    console.print(Panel(summary, title="Test All", style=style))

@cli.command(name="diff_all")
def diff_all():
    """Show diffs for all challenges that differ from reference answers."""
    console = Console()
    challenges = get_challenges()
    diffs = []
    identical = 0
    for ch in challenges:
        out, code = get_solution_diff(ch)
        if code == 0:
            identical += 1
        elif code == 1:
            diffs.append(f"[bold]{ch}[/bold]\n{out}")
        else:
            diffs.append(f"[bold]{ch}[/bold]: {out}")
    if not diffs:
        console.print(Panel(f"All {identical} challenge solutions match reference answers.", style="green", title="Diff All"))
    else:
        body = f"Identical: {identical} | With differences: {len(diffs)}\n\n" + "\n".join(diffs)
        console.print(Panel(body, style="cyan", title="Diff All"))

if __name__ == "__main__":
    cli()