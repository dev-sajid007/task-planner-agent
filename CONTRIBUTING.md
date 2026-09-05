# অবদান নির্দেশিকা

> Agent Task Runner এ অবদান রাখার নিয়ম — বাংলায়

---

## ১. স্বাগত

এই প্রজেক্টে অবদান রাখতে আগ্রহী হওয়ার জন্য ধন্যবাদ! ছোট PR ও ভালো ডকুমেন্টেশনই এই প্রজেক্টের মূল শক্তি।

---

## ২. শুরু করার আগে

- **Issue খুঁজুন:** `GitHub Issues` এ existing issue আছে কিনা দেখুন
- **নতুন ফিচার:** বড় ফিচারের জন্য আগে Issue খুলে আলোচনা করুন
- **পরিবেশ:** [docs/INSTALLATION.md](docs/INSTALLATION.md) অনুযায়ী `uv sync` করে পরিবেশ তৈরি করুন

---

## ৩. ডেভেলপমেন্ট সেটআপ

```bash
git clone https://github.com/dev-sajid007/task-planner-agent.git
cd task-planner-agent
uv sync
source .venv/bin/activate
```

---

## ৪. ব্রাঞ্চ ও কমিট

### ব্রাঞ্চ নাম

- `feat/xxx` — নতুন ফিচার (যেমন `feat/http-tool`)
- `fix/xxx` — বাগ ফিক্স (যেমন `fix/registry-get`)
- `docs/xxx` — ডকুমেন্টেশন (যেমন `docs/bangla-readme`)
- `refactor/xxx` — রিফ্যাক্টর

```bash
git checkout -b feat/my-tool
```

### কমিট মেসেজ (Conventional Commits)

```
feat: MyTool যোগ
fix: FileTool এ parent mkdir ব্যর্থতা সমাধান
docs: USAGE.md এ বাংলা উদাহরণ যোগ
refactor: Executor prefix পার্সিং সরলীকরণ
```

---

## ৫. কোড স্টাইল

- **Python:** `>=3.11`, `black`/`ruff` থাকলে চালান (বর্তমানে বাধ্যতামূলক নয়)
- **টাইপ হিন্ট:** নতুন কোডে `str`, `Optional[str]`, `list[str]` ব্যবহার করুন
- **ডকস্ট্রিং:** বাংলায় বা ইংরেজিতে সংক্ষিপ্ত, কোড আইডেন্টিফায়ার ইংরেজিতে
- **ফাইল রেফারেন্স:** নতুন কম্পোনেন্ট যোগ করলে `candidate.architecture.json` এর `sources` আপডেট করুন

---

## ৬. নতুন টুল যোগ

1. `src/agent_task_runner/tools/my_tool.py` তৈরি
2. `src/agent_task_runner/executor/executor.py:10` এ `register`
3. `execute()` এ prefix হ্যান্ডল
4. `docs/API.md` ও `docs/USAGE.md` আপডেট
5. উদাহরণ PR-এ `task-runner "mytool: arg"` আউটপুট দিন

---

## ৭. ডকুমেন্টেশন

- সব ডক **বাংলায়**, কোড/কমান্ড ইংরেজিতে
- `README.md` আপডেট করলে `docs/` লিংক ভাঙেনি তা যাচাই করুন
- আর্কিটেকচার পরিবর্তন করলে `docs/ARCHITECTURE.md` ও `candidate.architecture.json` একসাথে আপডেট করুন, তারপর:

```bash
node bin/archify.mjs validate architecture candidate.architecture.json --quality showcase --repo-root . --json
node bin/archify.mjs deliver architecture candidate.architecture.json agent-task-runner.html --quality showcase --repo-root .
```

---

## ৮. Pull Request

- **ছোট PR:** একটি PR এ একটি ফিচার/ফিক্স
- **বর্ণনা:** কী পরিবর্তন, কেন, কীভাবে টেস্ট করেছেন
- **টেস্ট:** `uv run task-runner "test"` চালিয়ে `output/main.py` যাচাই, সম্ভব হলে `pytest`
- **স্ক্রিনশট:** CLI আউটপুট বা ডায়াগ্রাম পরিবর্তন হলে PNG যোগ করুন

---

## ৯. রিপোর্ট

- **বাগ:** Issue এ `steps to reproduce`, `expected vs actual`, `python --version` দিন
- **ফিচার রিকোয়েস্ট:** ব্যবহারের উদাহরণ সহ বর্ণনা

---

## ১০. আচরণবিধি

সম্মানজনক, গঠনমূলক আলোচনা — অপ্রাসঙ্গিক মন্তব্য এড়িয়ে চলুন।

---

ধন্যবাদ! আপনার অবদান এই প্রজেক্টকে আরও ভালো করবে।
