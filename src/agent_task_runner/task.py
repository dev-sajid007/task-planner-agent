from dataclasses import dataclass, field
from uuid import uuid4
from typing import Optional


@dataclass
class Task:
    description: str
    id: str = field(default_factory=lambda: str(uuid4())[:8])
    status: str = "pending"
    result: Optional[str] = None
    error: Optional[str] = None

    def start(self):
        self.status = "running"

    def complete(self, result: str):
        self.status = "completed"
        self.result = result

    def fail(self, error: str):
        self.status = "failed"
        self.error = error