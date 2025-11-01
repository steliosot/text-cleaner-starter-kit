# 🧹 Text Cleaner (Simple)

A super simple Python project for beginners to practice cleaning text files.

It reads text from `data/raw/input.txt`, applies basic cleaning rules from `cleaner/rules.yaml`, and saves the result to `data/clean/output.txt`.

---

## 📦 Project Structure
```
text-cleaner-simple/
├─ cleaner/
│  ├─ clean.py          # main script
│  ├─ rules.yaml        # basic cleaning rules
├─ data/
│  ├─ raw/
│  │  └─ input.txt      # sample text file
│  └─ clean/
│     └─ output.txt     # result after cleaning
├─ tests/
│  └─ test_clean.py     # very basic test
```

---

## ▶️ How to Run

1. Open a terminal inside the project folder.
2. Run the cleaner:
   ```bash
   python3 cleaner/clean.py
   ```
3. The cleaned text will appear in:
   ```
   data/clean/output.txt
   ```

---

## 🧠 What It Does
- Removes extra spaces from each line  
- Converts all text to lowercase  
- Skips empty lines  

You can change these behaviors in `cleaner/rules.yaml`:
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

Enjoy learning Python with this tiny project!
