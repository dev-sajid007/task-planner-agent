from agent_task_runner.task import Task
from agent_task_runner.planner.planner import Planner
from agent_task_runner.executor.executor import Executor


def run_task(description: str):
    task = Task(description)

    print(f"Task ID: {task.id}")
    print(f"Task: {task.description}")
    print(f"Status: {task.status}")

    planner = Planner()
    executor = Executor()

    plan = planner.create_plan(task.description)

    print("\nPlan:")

    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")

    task.start()

    print(f"\nStatus: {task.status}")
    print("\nExecution:")

    for step in plan:
        executor.execute(step)

    task.complete("Task executed successfully.")

    print(f"\nStatus: {task.status}")
    print(f"Result: {task.result}")

    return task