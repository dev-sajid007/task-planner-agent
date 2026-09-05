from agent_task_runner.planner.plan import PlanStep
from agent_task_runner.registry.tool_registry import ToolRegistry


class Executor:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, step: PlanStep) -> str:
        print(
            f"Executing: {step.tool}.{step.action}"
        )

        tool = self.registry.get(step.tool)

        if tool is None:
            return f"Error: tool '{step.tool}' not found"

        return tool.execute(
            step.action,
            step.arguments,
        )