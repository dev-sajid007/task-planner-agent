# ইনস্টলেশন গাইড

> Agent Task Runner ইনস্টল ও পরিবেশ সেটআপ — uv (প্রস্তাবিত) ও pip উভয় পদ্ধতি

---

## ১. প্রয়োজনীয়তা

- **Python:** `>=3.11` — `pyproject.toml:9`
- **OS:** Linux / macOS / Windows (WSL প্রস্তাবিত)
- **প্যাকেজ ম্যানেজার:** `uv` >=0.4 অথবা `pip` >=23
- **Git**

যাচাই:

```bash
python --version  # Python 3.11.x
uv --version      # uv 0.4.x (যদি থাকে)
```

---

## ২. ক্লোন

```bash
git clone https://github.com/dev-sajid007/task-planner-agent.git
cd task-planner-agent
# অথবা বর্তমান ফোল্ডার যদি ইতিমধ্যে ক্লোন করা থাকে
cd /home/dev_sajid/Desktop/training/agent-task-runner
```

---

## ৩. পদ্ধতি A — uv (প্রস্তাবিত, দ্রুত)

`uv` স্বয়ংক্রিয়ভাবে `.venv` তৈরি ও `uv.lock` থেকে নির্ভরতা ইনস্টল করে।

```bash
# 1. uv ইনস্টল (যদি না থাকে)
curl -LsSf https://astral.sh/uv/install.sh | sh
# অথবা pipx
pipx install uv

# 2. নির্ভরতা ইনস্টল
uv sync

# 3. যাচাই — CLI কাজ করছে কিনা
uv run task-runner --help
uv run task-runner "পরীক্ষা টাস্ক"

# 4. (ঐচ্ছিক) .venv activate
source .venv/bin/activate
task-runner --help
```

**`pyproject.toml` নির্ভরতা:** `typer>=0.27.2` স্বয়ংক্রিয়ভাবে ইনস্টল হয়।

---

## ৪. পদ্ধতি B — pip + venv

```bash
# 1. venv তৈরি
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 2. pip আপগ্রেড
pip install --upgrade pip

# 3. ইনস্টল
pip install -e .
# অথবা build থেকে
pip install .

# 4. যাচাই
task-runner --help
python -c "from agent_task_runner.main import run_task; print('ok')"
```

---

## ৫. এন্ট্রি পয়েন্ট যাচাই

`pyproject.toml:14-15`:

```toml
[project.scripts]
task-runner = "agent_task_runner.cli:app"
```

যাচাই:

```bash
which task-runner          # .venv/bin/task-runner
task-runner --help         # Typer help দেখাবে
python -m agent_task_runner.cli --help
```

---

## ৬. সাধারণ সমস্যা

| সমস্যা | সমাধান |
|---|---|
| `task-runner: command not found` | `.venv` activate করুন বা `uv run task-runner` ব্যবহার করুন |
| `Python 3.11 required` | `python --version` যাচাই, `uv python pin 3.11` বা `pyenv` ব্যবহার |
| `typer not found` | `uv sync` বা `pip install typer` পুনরায় চালান |
| `output/main.py` permission error | `ls -ld output` যাচাই, `chmod 755 output` |

---

## ৭. আনইনস্টল

```bash
# uv
rm -rf .venv uv.lock  # uv.lock রাখতে চাইলে মুছবেন না
# pip
pip uninstall agent-task-runner
deactivate
rm -rf .venv
```

---

## ৮. পরবর্তী ধাপ

- ব্যবহার: [USAGE.md](USAGE.md)
- আর্কিটেকচার: [ARCHITECTURE.md](ARCHITECTURE.md)
- API: [API.md](API.md)
