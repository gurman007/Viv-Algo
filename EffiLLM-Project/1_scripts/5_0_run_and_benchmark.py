import json
import time
import importlib.util
from pathlib import Path
import threading

# === CONFIGURATION ===
BENCHMARK_FILE = "yo_benchmark_testcases.json"
MODEL_NAME = "mistral"
TIMEOUT = 2  # seconds

def run_with_timeout(script_path, func_name, input_args, timeout=TIMEOUT):
    result_container = {}

    def runner():
        try:
            spec = importlib.util.spec_from_file_location("solution", script_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            solution = mod.Solution()
            func = getattr(solution, func_name)
            result_container["output"] = func(*input_args)
        except Exception as e:
            result_container["output"] = "__EXCEPTION__"

    thread = threading.Thread(target=runner)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return "__TIMEOUT__"
    return result_container.get("output", "__EXCEPTION__")

def main():
    with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
        benchmark = json.load(f)

    results_by_problem = {}

    for problem_key, entry in benchmark.items():
        func_name = entry["function"]
        testcases = entry["testcases"]

        num = int(problem_key.split("_")[1])
        if num <= 8:
            folder = "easy"
            mapped_id = problem_key
        elif 9 <= num <= 18:
            folder = "medium"
            mapped_id = f"dp_{num - 8:03d}"
        else:
            folder = "hard"
            mapped_id = f"dp_{num - 18:03d}"

        script_path = Path("2_problems") / folder / mapped_id / f"{MODEL_NAME}.py"
        if not script_path.exists():
            results_by_problem[problem_key] = {"pass": 0, "fail": 0, "error": len(testcases), "total": len(testcases)}
            continue

        passed, failed, error = 0, 0, 0

        for test in testcases:
            result = run_with_timeout(str(script_path), func_name, test["input"])
            if result == "__TIMEOUT__" or result == "__EXCEPTION__":
                error += 1
            elif result == test["expected"]:
                passed += 1
            else:
                failed += 1

        results_by_problem[problem_key] = {
            "pass": passed,
            "fail": failed,
            "error": error,
            "total": len(testcases)
        }

    print(f"\n📊 Benchmark Summary for {MODEL_NAME.upper()}:\n")
    for k in sorted(results_by_problem.keys()):
        r = results_by_problem[k]
        print(f"{k} → ✅ {r['pass']:3d} | ❌ {r['fail']:3d} | 🚫 {r['error']:3d} | Total: {r['total']}")

if __name__ == "__main__":
    main()
