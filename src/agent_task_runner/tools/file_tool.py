from pathlib import Path

from agent_task_runner.tools.base import Tool


class FileTool(Tool):

    @property
    def name(self) -> str:
        return "file"

    @property
    def description(self) -> str:
        return "Create, read, write and manage files"

    def execute(self, action: str, arguments: dict) -> str:

        if action == "create":
            return self.create_file(arguments["path"])

        if action == "read":
            return self.read_file(arguments["path"])

        if action == "write":
            return self.write_file(
                arguments["path"],
                arguments["content"],
            )

        return f"Error: unknown file action '{action}'"

    def create_file(self, path: str) -> str:
        file_path = Path(path)

        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch(exist_ok=True)

        return f"Created file: {file_path}"

    def read_file(self, path: str) -> str:
        file_path = Path(path)

        if not file_path.exists():
            return f"Error: file not found: {file_path}"

        return file_path.read_text()

    def write_file(self, path: str, content: str) -> str:
        file_path = Path(path)

        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)

        return f"Wrote file: {file_path}"

