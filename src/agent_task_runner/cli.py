import typer

from agent_task_runner.main import run_task

app = typer.Typer()


@app.command()
def run_agent_task(task: str):
    run_task(task)