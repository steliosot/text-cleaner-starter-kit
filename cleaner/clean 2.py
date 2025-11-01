# Very simple text cleaner
# Reads input.txt, cleans each line, and writes cleaned_output.txt

import yaml

# Load rules
with open("cleaner/rules.yaml", "r", encoding="utf-8") as f:
    rules = yaml.safe_load(f)

# Read input
with open("data/raw/input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned = []

for line in lines:
    text = line
    if rules.get("strip", True):
        text = text.strip()
    if rules.get("lower", True):
        text = text.lower()
    if rules.get("remove_empty", True) and text == "":
        continue
    cleaned.append(text)

# Write output
with open("data/clean/output.txt", "w", encoding="utf-8") as f:
    for line in cleaned:
        f.write(line + "\n")

print("✅ Done! See data/clean/output.txt")
