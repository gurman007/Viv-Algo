import os

# === Config ===
base_path = "2_problems"
levels = ["easy", "medium", "hard"]
filename = "grok.py"

# === Create grok.py if missing ===
created = 0
for level in levels:
    level_dir = os.path.join(base_path, level)
    if not os.path.exists(level_dir):
        continue

    for folder in sorted(os.listdir(level_dir)):
        problem_path = os.path.join(level_dir, folder)
        grok_file = os.path.join(problem_path, filename)

        if not os.path.exists(grok_file):
            with open(grok_file, "w", encoding="utf-8") as f:
                f.write("# Placeholder for Grok-3 generated solution\n\nclass Solution:\n    pass\n")
            created += 1
            print(f"✅ Created: {grok_file}")
        else:
            print(f"🟡 Already exists: {grok_file}")

print(f"\n📦 Done! Total new `grok.py` files created: {created}")
