from dataclasses import dataclass


@dataclass
class Task:
    description: str
    status: str = "pending"

    def start(self):
        self.status = "running"

    def complete(self):
        self.status = "completed"

    def fail(self):
        self.status = "failed"
