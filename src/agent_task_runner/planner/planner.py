class Planner:

    def create_plan(self,task:str) -> list[str] :
        return [
            f"Understand task: {task}",
            "create_file: output/main.py",
            "Verify result",
        ]