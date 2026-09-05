from dataclasses import dataclass


@dataclass
class PlanStep:
    tool: str
    action: str
    arguments: dict


@dataclass
class Plan:
    steps: list[PlanStep]