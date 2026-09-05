# ব্যবহার নির্দেশিকা

> CLI ও Python API — উদাহরণসহ

---

## ১. CLI ব্যবহার

### ১.১ সাহায্য

```bash
task-runner --help
uv run task-runner --help
```

### ১.২ মৌলিক কমান্ড

```bash
# সাধারণ
task-runner "একটি হ্যালো ওয়ার্ল্ড ফাইল তৈরি করো"

# ইংরেজি বর্ণনা
task-runner "Create a login page"

# পাথ সহ
task-runner "output/docs/README.md ফাইল তৈরি করো"
```

### ১.৩ আউটপুট

```bash
$ task-runner "demo"

Task ID: f3a9c1d2
Task: demo
Status: pending

Plan:
1. Understand task: demo
2. create_file: output/main.py
3. Verify result

Status: running

Execution:
Executing: Understand task: demo
Executing: create_file: output/main.py
Executing: Verify result

Status: completed
Result: Task executed successfully.
```

ফলাফল: `output/main.py` তৈরি হয় (খালি ফাইল, `FileTool` default `content=""`).

### ১.৪ টিপস

- বর্ণনায় স্পেস থাকলে উদ্ধৃতি চিহ্ন (`"..."`) ব্যবহার করুন
- `output/` ফোল্ডার স্বয়ংক্রিয়ভাবে তৈরি হয় — `FileTool` `mkdir(parents=True)` করে

---

## ২. Python API

### ২.১ `run_task()`

`src/agent_task_runner/main.py:6`:

```python
from agent_task_runner.main import run_task

# সাধারণ
task = run_task("ডেটা প্রসেসিং স্ক্রিপ্ট তৈরি করো")
print(task.id)          # f3a9c1d2 (uuid4[:8])
print(task.status)      # completed
print(task.result)      # Task executed successfully.
print(task.description)

# এরর হ্যান্ডলিং (বর্তমানে always success)
if task.status == "completed":
    print("সফল")
```

### ২.২ `Task` সরাসরি

`src/agent_task_runner/task.py:6`:

```python
from agent_task_runner.task import Task

t = Task("পরীক্ষা")
print(t.status)  # pending
print(t.id)      # 8-char uuid

t.start()
print(t.status)  # running

t.complete("done")
print(t.status, t.result)  # completed done

# ব্যর্থতা
t2 = Task("fail demo")
t2.start()
t2.fail("something went wrong")
print(t2.status, t2.error)  # failed something went wrong
```

### ২.৩ `Planner`

`src/agent_task_runner/planner/planner.py:1`:

```python
from agent_task_runner.planner.planner import Planner

planner = Planner()
plan = planner.create_plan("আমার টাস্ক")
print(plan)
# ['Understand task: আমার টাস্ক', 'create_file: output/main.py', 'Verify result']

# প্রতিটি step Executor এ পাঠানো হয়
for step in plan:
    print(step)
```

### ২.৪ `Executor` ও `ToolRegistry`

`src/agent_task_runner/executor/executor.py:5` এবং `registry/tool_registry.py:1`:

```python
from agent_task_runner.executor.executor import Executor
from agent_task_runner.registry.tool_registry import ToolRegistry

executor = Executor()
result = executor.execute("create_file: output/test.py")
print(result)  # Created file: output/test.py

result2 = executor.execute("Verify result")
print(result2)  # Completed: Verify result

# Registry সরাসরি
registry = ToolRegistry()
from agent_task_runner.tools.file_tool import FileTool
registry.register("file", FileTool())
tool = registry.get("file")
print(registry.has("file"))  # True
print(registry.list_tools()) # ['file']
```

### ২.৫ `FileTool`

`src/agent_task_runner/tools/file_tool.py:4`:

```python
from agent_task_runner.tools.file_tool import FileTool

tool = FileTool()
tool.create_file("output/hello.py", content="print('hello')")
tool.create_file("output/nested/deep/file.txt", content="hi")
# parent ফোল্ডার স্বয়ংক্রিয়ভাবে তৈরি হয়
```

---

## ৩. নতুন টুল যোগ (এক্সটেনশন)

```python
# src/agent_task_runner/tools/my_tool.py
class MyTool:
    def do_something(self, arg: str) -> str:
        return f"Done: {arg}"

# src/agent_task_runner/executor/executor.py — __init__ এ
from agent_task_runner.tools.my_tool import MyTool
self.registry.register("mytool", MyTool())

# executor.py — execute() এ নতুন prefix
if step.startswith("mytool:"):
    arg = step.split(":", 1)[1].strip()
    tool = self.registry.get("mytool")
    return tool.do_something(arg)
```

তারপর:

```bash
task-runner "mytool: hello world"
```

---

## ৪. আউটপুট যাচাই

```bash
ls -R output
cat output/main.py
```

ডিফল্ট `output/main.py` খালি থাকে — `planner.py:6` এ `content=""`। কন্টেন্ট যোগ করতে `FileTool.create_file(path, content="...")` এ কন্টেন্ট পাস করুন বা Planner কে কন্টেন্ট জেনারেট করতে সম্প্রসারিত করুন।

---

## ৫. পরবর্তী

- আর্কিটেকচার গভীরে: [ARCHITECTURE.md](ARCHITECTURE.md)
- API রেফারেন্স: [API.md](API.md)
