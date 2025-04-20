import json
import re

# === Load selected_dp_problems.json ===
with open("selected_dp_problems.json", "r", encoding="utf-8") as f:
    selected = json.load(f)

# === Helper to parse assert lines into inputs and expected ===
def extract_testcases(assert_block, func_name):
    testcases = []
    pattern = re.compile(rf"assert\s+{re.escape(f'solution.{func_name}')}(\(.*?\))\s*==\s*(.+)")
    for line in assert_block.strip().splitlines():
        line = line.strip()
        if not line.startswith("assert"):
            continue
        match = pattern.match(line)
        if match:
            args = match.group(1)
            expected = match.group(2)
            try:
                # Fix binary literals like 0110 → "0110"
                args = re.sub(r'(?<!")\b0\d+\b(?!")', lambda m: f'"{m.group(0)}"', args)
                input_data = eval(f"[{args[1:-1]}]")  # convert "(x, y)" → [x, y]
                expected_output = eval(expected)
                testcases.append({"input": input_data, "expected": expected_output})
            except Exception as e:
                print(f"⚠️ Skipping malformed line: {line} → {e}")
    return testcases

# === Build final benchmark dict ===
benchmark = {}
counter = 1

for level in ["Easy", "Medium", "Hard"]:
    for problem in selected[level]:
        func_name = None
        if "canonical_solution" in problem:
            match = re.search(r"def\s+(\w+)\s*\(", problem["canonical_solution"])
            if match:
                func_name = match.group(1)

        if not func_name:
            continue

        testcase_block = problem.get("test_case", "")
        parsed_cases = extract_testcases(testcase_block, func_name)

        benchmark[f"dp_{counter:03d}"] = {
            "function": func_name,
            "testcases": parsed_cases
        }
        counter += 1

# === Save to JSON ===
with open("yo_benchmark_testcases_full.json", "w", encoding="utf-8") as f:
    json.dump(benchmark, f, indent=2)

print("✅ yo_benchmark_testcases_full.json generated successfully.")
