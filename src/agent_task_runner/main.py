from agent_task_runner.task import Task
from agent_task_runner.planner.planner import Planner
from agent_task_runner.executor.executor import Executor
from agent_task_runner.registry.tool_registry import ToolRegistry
from agent_task_runner.tools.file_tool import FileTool


def run_task(description: str):
    task = Task(description)

    print(f"Task ID: {task.id}")
    print(f"Task: {task.description}")
    print(f"Status: {task.status}")

    planner = Planner()

    registry = ToolRegistry()
    registry.register(FileTool())

    executor = Executor(registry)

    plan = planner.create_plan(task.description)

    print("\nPlan:")

    for index, step in enumerate(plan.steps, start=1):
        print(
            f"{index}. "
            f"{step.tool}.{step.action}"
        )

    task.start()

    print(f"\nStatus: {task.status}")
    print("\nExecution:")

    for step in plan.steps:
        result = executor.execute(step)
        print(result)

    task.complete("Task executed successfully.")

    print(f"\nStatus: {task.status}")
    print(f"Result: {task.result}")

    return task