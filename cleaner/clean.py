# Very simple text cleaner for beginners
# Reads input.txt, cleans each line, and writes output.txt

import yaml
from pathlib import Path

# Load rules from YAML file
rules_path = Path("cleaner/rules.yaml")
with rules_path.open("r", encoding="utf-8") as f:
    rules = yaml.safe_load(f)

# Read input file
input_path = Path("data/raw/input.txt")
with input_path.open("r", encoding="utf-8") as f:
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

# Write output file
output_path = Path("data/clean/output.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
with output_path.open("w", encoding="utf-8") as f:
    for line in cleaned:
        f.write(line + "\n")

print("✅ Cleaning complete! Check data/clean/output.txt")
