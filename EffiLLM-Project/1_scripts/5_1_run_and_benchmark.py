import json
import time
import importlib.util
from pathlib import Path
import csv
import os

# === Configuration ===
MODEL_NAME = "claude"
BENCHMARK_FILE = "benchmark_testcases.json"

# === Difficulty level mapping ===
DIFFICULTY_MAP = {
    "easy": range(1, 9),
    "medium": range(9, 19),
    "hard": range(19, 29),
}

def get_difficulty(problem_key):
    num = int(problem_key.split("_")[1])
    for diff, rng in DIFFICULTY_MAP.items():
        if num in rng:
            return diff
    return None

def map_to_actual_folder(problem_key):
    num = int(problem_key.split("_")[1])
    difficulty = get_difficulty(problem_key)
    if difficulty == "easy":
        return Path("2_problems/easy") / f"dp_{num:03d}"
    elif difficulty == "medium":
        mapped = num - 8
        return Path("2_problems/medium") / f"dp_{mapped:03d}"
    elif difficulty == "hard":
        mapped = num - 18
        return Path("2_problems/hard") / f"dp_{mapped:03d}"
    else:
        return None

def load_solution(script_path):
    spec = importlib.util.spec_from_file_location("solution", script_path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        return mod.Solution()
    except Exception as e:
        return str(e)

# === Load benchmark data ===
with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
    benchmark = json.load(f)

# === Run benchmark ===
results = []

for problem_key in sorted(benchmark.keys()):
    entry = benchmark[problem_key]
    function_name = entry["function"]
    testcases = entry["testcases"]
    folder = map_to_actual_folder(problem_key)

    if not folder:
        results.append((problem_key, MODEL_NAME, "❌ Invalid folder mapping", None, None, False))
        continue

    script_path = folder / f"{MODEL_NAME}.py"
    if not script_path.exists():
        results.append((problem_key, MODEL_NAME, "❌ File missing", None, None, False))
        continue

    solution = load_solution(script_path)
    if isinstance(solution, str):
        results.append((problem_key, MODEL_NAME, f"❌ Load error: {solution}", None, None, False))
        continue

    func = getattr(solution, function_name, None)
    if not callable(func):
        results.append((problem_key, MODEL_NAME, f"❌ No method `{function_name}`", None, None, False))
        continue

    for test in testcases:
        start = time.perf_counter()
        try:
            output = func(*test["input"])
            elapsed = time.perf_counter() - start
            is_correct = output == test["expected"]
            results.append((problem_key, MODEL_NAME, output, elapsed, test["expected"], is_correct))
        except Exception as e:
            results.append((problem_key, MODEL_NAME, f"❌ Exception: {e}", None, test["expected"], False))

# === Save results to CSV ===
os.makedirs("3_data", exist_ok=True)
csv_file = "3_data/results_claude.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "problem",
        "model",
        "function",
        "input",
        "expected",
        "output",
        "is_correct",
        "time_taken"
    ])
    for r in results:
        writer.writerow([
            r[0],
            r[1],
            benchmark[r[0]]["function"],
            str(r[4] if r[5] else ""),
            r[4],
            r[2],
            r[5],
            r[3]
        ])

# === Print summary ===
print("\nBenchmark Results for claude.py:")
print("-" * 100)
for r in results:
    print(f"{r[0]} → Output: {r[2]} | Time: {r[3]}s | Expected: {r[4]} | ✅ {r[5]}")

print(f"\n✅ Claude results saved to {csv_file}")
