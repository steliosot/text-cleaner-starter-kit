# 🧹 Text Cleaner (Simple + Virtual Environment)

A super simple Python project for beginners to practice cleaning text files **and using virtual environments (venv)**.

It reads text from `data/raw/input.txt`, applies basic cleaning rules from `cleaner/rules.yaml`, and saves the result to `data/clean/output.txt`.

---

## 📦 Project Structure
```
text-cleaner-simple-venv/
├─ cleaner/
│  ├─ clean.py          # main script
│  ├─ rules.yaml        # basic cleaning rules
├─ data/
│  ├─ raw/
│  │  └─ input.txt      # sample text file
│  └─ clean/
│     └─ output.txt     # result after cleaning
├─ tests/
│  └─ test_clean.py     # simple test
├─ requirements.txt     # dependencies
```

---

## 🧰 Setup Virtual Environment

Before running the project, create and activate a **virtual environment** to keep your workspace clean.

### 1️⃣ Create a venv
```bash
python3 -m venv .venv
```

### 2️⃣ Activate it
**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Cleaner
After activating your venv, run:
```bash
python3 cleaner/clean.py
```

The cleaned text will appear in:
```
data/clean/output.txt
```

---

## 🧠 What It Does
- Removes extra spaces from each line  
- Converts text to lowercase  
- Skips empty lines  

You can change these settings in `cleaner/rules.yaml`:
```yaml
lower: true
strip: true
remove_empty: true
```

---

## 🧪 Optional Test
If you want to check that everything works:
```bash
python3 -m pytest -q
```

---

## ✨ Example
**Input (`data/raw/input.txt`):**
```
  Hello WORLD  

This   is   a SIMPLE example
```

**Output (`data/clean/output.txt`):**
```
hello world
this   is   a simple example
```

---

Enjoy learning Python and virtual environments! 🎓
