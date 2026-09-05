from agent_task_runner.task import Task


def run_task(description: str):
    task = Task(description)

    print(f"Task: {task.description}")
    print(f"Status: {task.status}")

    task.start()

    print(f"Status: {task.status}")

    task.complete()

    print(f"Status: {task.status}")

    return task