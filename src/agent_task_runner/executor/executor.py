from agent_task_runner.tools.file_tool import FileTool

class Executor:
    def __init__(self):
        self.file_tool = FileTool()

    def execute(self, step: str) -> str:
        print(f"Executing: {step}")

        if step.startswith("create_file:"):
            path = step.split(":", 1)[1].strip()

            return self.file_tool.create_file(path)
        return f"Completed: {step}"