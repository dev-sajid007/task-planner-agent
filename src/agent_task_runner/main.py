from agent_task_runner.task import Task


def run_task(description: str):
    task = Task(description=description)
    print(f"Task: {task.description}")
    print(f"Status: {task.status}")

    task.status = "completed"


    return task
