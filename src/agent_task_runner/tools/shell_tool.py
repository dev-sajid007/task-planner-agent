import subprocess

from agent_task_runner.tools.base import Tool


class ShellTool(Tool):
    
    @property
    def name(self) -> str:
        return "shell"
    
    
    @property
    def description(self) -> str:
        return "Execute shell commands"
    
    def execute(self, action: str, arguments: dict) -> str:
        if action == "run":
            return self.run_command(arguments["command"])
        
        return f"Error: unknown shell action '{action}'"
    
    def run_command(self, command: str) -> str:
    
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                return (
                    f"Error: command failed\n"
                    f"{result.stderr.strip()}"
                )

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            return "Error: command timed out"