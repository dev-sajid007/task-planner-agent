# পরিবর্তন লগ

> Agent Task Runner — সব উল্লেখযোগ্য পরিবর্তন বাংলায়

ফরম্যাট: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) অনুসরণ, [Semantic Versioning](https://semver.org/lang/en/)।

---

## [0.1.0] - 2026-09-05

### যোগ করা হয়েছে
- **Core:** `Task` dataclass (`task.py:6`) — `pending → running → completed/failed`, `uuid4[:8]`
- **Planner:** `Planner.create_plan()` — ৩ ধাপের fixed plan (`planner.py:1`)
- **Executor:** `Executor.execute()` — `create_file:` prefix, `ToolRegistry` resolve (`executor.py:5`)
- **Registry:** `ToolRegistry` — `register/get/has/list_tools` (`registry/tool_registry.py:1`)
- **Tool:** `FileTool.create_file()` — `Path.mkdir(parents)+write_text` (`tools/file_tool.py:4`)
- **Orchestrator:** `run_task()` — Task lifecycle + Planner/Executor সমন্বয় (`main.py:6`)
- **CLI:** `run_agent_task` — Typer entry `task-runner` (`cli.py:8`, `pyproject.toml:14`)
- **ডকুমেন্টেশন (বাংলা):** `README.md`, `docs/ARCHITECTURE.md`, `docs/INSTALLATION.md`, `docs/USAGE.md`, `docs/API.md`, `CONTRIBUTING.md`, `CHANGELOG.md`
- **ডায়াগ্রাম:** Archify showcase — `candidate.architecture.json` (8 কম্পোনেন্ট, 2 boundary, 8 connection), `agent-task-runner.html` (viewBox 1280×680, 9/9 checks pass, visual-check pass 1440×900/1920×1080)

### পরিবর্তন
- `README.md` খালি থেকে পূর্ণ বাংলা README তে রূপান্তর
- `.gitignore` এ Python cache/venv

### জানা সীমাবদ্ধতা
- `FileTool` শুধু write, read/delete নেই
- Planner fixed — LLM/dynamic plan নেই
- `output/main.py` default খালি

---

## [Unreleased]

### পরিকল্পিত
- নতুন টুল (`http`, `db`) — Registry সম্প্রসারণ
- Async Executor
- Plan validation ও persistence
