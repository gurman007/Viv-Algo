import json
from pathlib import Path

# Load selected_dp_problems.json
with open("selected_dp_problems.json", "r", encoding="utf-8") as f:
    selected = json.load(f)

# Folder mapping
level_map = {
    "Easy": "easy",
    "Medium": "medium",
    "Hard": "hard"
}

# Output folder
output_dir = Path("prompts_ready")
output_dir.mkdir(exist_ok=True)

# Save cleaned markdown prompts
for level in ["Easy", "Medium", "Hard"]:
    prefix = level_map[level]
    for i, problem in enumerate(selected[level], 1):
        filename = f"{prefix}_dp_{i:03d}.txt"
        filepath = output_dir / filename
        markdown = problem.get("markdown_description", "").strip()

        # Skip image links
        cleaned_lines = []
        for line in markdown.splitlines():
            if not line.strip().startswith("![]("):
                cleaned_lines.append(line)

        # Write to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(cleaned_lines))

print("✅ Cleaned prompts saved to prompts_ready/ (images skipped).")
