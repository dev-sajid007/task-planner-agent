# API রেফারেন্স

> মডিউল ভিত্তিক — সোর্স লাইন রেফারেন্স সহ

---

## ১. `agent_task_runner.task` — Task Model

**ফাইল:** `src/agent_task_runner/task.py:1`

```python
from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Task:
    description: str
    id: str = field(default_factory=lambda: str(uuid4())[:8])
    status: str = "pending"
    result: Optional[str] = None
    error: Optional[str] = None

    def start(self): ...
    def complete(self, result: str): ...
    def fail(self, error: str): ...
```

| ফিল্ড/মেথড | ধরন | বর্ণনা |
|---|---|---|
| `description` | `str` | টাস্কের বর্ণনা, `__init__` এ বাধ্যতামূলক |
| `id` | `str` | 8-char UUID, `uuid4()[:8]` |
| `status` | `str` | `pending` → `running` → `completed/failed` |
| `result` | `Optional[str]` | সাফল্যের ফলাফল |
| `error` | `Optional[str]` | ব্যর্থতার বার্তা |
| `start()` | `-> None` | `status = "running"` — `task.py:14` |
| `complete(result)` | `-> None` | `status = "completed"`, `result` সেট — `task.py:17` |
| `fail(error)` | `-> None` | `status = "failed"`, `error` সেট — `task.py:21` |

---

## ২. `agent_task_runner.planner.planner` — Planner

**ফাইল:** `src/agent_task_runner/planner/planner.py:1`

```python
class Planner:
    def create_plan(self, task: str) -> list[str]:
        return [
            f"Understand task: {task}",
            "create_file: output/main.py",
            "Verify result",
        ]
```

| মেথড | সিগনেচার | বর্ণনা |
|---|---|---|
| `create_plan` | `(task: str) -> list[str]` | ৩ ধাপের fixed plan ফেরত দেয় |

**নোট:** বর্তমানে deterministic, ভবিষ্যতে LLM বা টেমপ্লেট ভিত্তিক করা যায়।

---

## ৩. `agent_task_runner.executor.executor` — Executor

**ফাইল:** `src/agent_task_runner/executor/executor.py:1`

```python
class Executor:
    def __init__(self):
        self.registry = ToolRegistry()
        self.registry.register("file", FileTool())

    def execute(self, step: str) -> str:
        print(f"Executing: {step}")
        if step.startswith("create_file:"):
            path = step.split(":", 1)[1].strip()
            tool = self.registry.get("file")
            if tool is None:
                return "Error: file tool not found"
            return tool.create_file(path)
        return f"Completed: {step}"
```

| মেথড | সিগনেচার | বর্ণনা |
|---|---|---|
| `__init__` | `() -> None` | Registry তৈরি ও `FileTool` রেজিস্টার |
| `execute` | `(step: str) -> str` | `create_file:` prefix হলে FileTool কল, না হলে `Completed: ...` |

---

## ৪. `agent_task_runner.registry.tool_registry` — ToolRegistry

**ফাইল:** `src/agent_task_runner/registry/tool_registry.py:1`

```python
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name: str, tool): ...
    def get(self, name: str): ...
    def has(self, name: str) -> bool: ...
    def list_tools(self): ...
```

| মেথড | সিগনেচার | বর্ণনা |
|---|---|---|
| `register` | `(name: str, tool) -> None` | নামে টুল রেজিস্টার |
| `get` | `(name: str) -> tool | None` | টুল ফেরত, না থাকলে `None` |
| `has` | `(name: str) -> bool` | টুল আছে কিনা |
| `list_tools` | `() -> list[str]` | রেজিস্টার্ড নামের তালিকা |

---

## ৫. `agent_task_runner.tools.file_tool` — FileTool

**ফাইল:** `src/agent_task_runner/tools/file_tool.py:1`

```python
from pathlib import Path

class FileTool:
    def create_file(self, path: str, content: str = "") -> str:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return f"Created file: {file_path}"
```

| মেথড | সিগনেচার | বর্ণনা |
|---|---|---|
| `create_file` | `(path: str, content: str = "") -> str` | parent ফোল্ডার তৈরি, ফাইল লেখা, `"Created file: ..."` ফেরত |

---

## ৬. `agent_task_runner.main` — Orchestrator

**ফাইল:** `src/agent_task_runner/main.py:1`

```python
def run_task(description: str):
    task = Task(description)
    print(f"Task ID: {task.id}")
    planner = Planner()
    executor = Executor()
    plan = planner.create_plan(task.description)
    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")
    task.start()
    for step in plan:
        executor.execute(step)
    task.complete("Task executed successfully.")
    return task
```

| ফাংশন | সিগনেচার | বর্ণনা |
|---|---|---|
| `run_task` | `(description: str) -> Task` | পূর্ণ প্রবাহ — Task তৈরি, plan, execute, complete, Task ফেরত |

**প্রিন্ট আউটপুট:** Task ID, Plan তালিকা, Execution লগ, Status/Result — `main.py:9-34`

---

## ৭. `agent_task_runner.cli` — CLI

**ফাইল:** `src/agent_task_runner/cli.py:1`

```python
import typer
from agent_task_runner.main import run_task

app = typer.Typer()

@app.command()
def run_agent_task(task: str):
    run_task(task)
```

| কমান্ড | সিগনেচার | বর্ণনা |
|---|---|---|
| `run_agent_task` | `(task: str)` | Typer কমান্ড, `task-runner` entry point |

**Entry point:** `pyproject.toml:14` — `task-runner = "agent_task_runner.cli:app"`

```bash
task-runner "my task"
uv run task-runner "my task"
python -m agent_task_runner.cli "my task"
```

---

## ৮. টাইপ ও কনভেনশন

- **Python:** `>=3.11`, `dataclass`, `pathlib`, `typing.Optional`
- **CLI:** `typer>=0.27.2`
- **ID:** `str(uuid4())[:8]` — 8-char hex
- **Status:** `pending | running | completed | failed`
- **Plan step:** `str` — `create_file:` prefix দিয়ে FileTool রাউটিং

---

> **রেফারেন্স:** সব `file:line` Archify `candidate.architecture.json` এর `sources` থেকে যাচাইকৃত।
