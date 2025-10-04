from human_eval.data import read_problems
import json

# Download and save HumanEval problems
print("Downloading HumanEval dataset...")
problems = read_problems()

# Save to a file for easy access
with open('humaneval_problems.json', 'w') as f:
    json.dump(problems, f, indent=2)

print(f"✅ Downloaded {len(problems)} problems")
print("✅ Saved to humaneval_problems.json")

# Show first problem as example
first_problem = list(problems.values())[0]
print("\n" + "="*60)
print("Example Problem:")
print("="*60)
print(first_problem['prompt'][:300] + "...")