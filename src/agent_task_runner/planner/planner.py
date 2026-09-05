from agent_task_runner.planner.plan import Plan, PlanStep


class Planner:

    def create_plan(self, task: str) -> Plan:
        return Plan(
            steps=[
                PlanStep(
                    tool="shell",
                    action="run",
                    arguments={
                        "command": "python --version"
                    },
                )
            ]
        )