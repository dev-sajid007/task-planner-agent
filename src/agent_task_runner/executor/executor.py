from agent_task_runner.registry.tool_registry import ToolRegistry


class Executor:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, step: str) -> str:
        print(f"Executing: {step}")

        if step.startswith("create_file:"):
            path = step.split(":", 1)[1].strip()

            tool = self.registry.get("file")

            if tool is None:
                return "Error: file tool not found"

            return tool.create_file(path)

        return f"Completed: {step}"