import pandas as pd
import json

# Load results
df = pd.read_csv("results/part1_results.csv")

# Find all failures
failures = df[df['passed'] == False].copy()

print("="*70)
print("FAILURE ANALYSIS")
print("="*70)

print(f"\nTotal experiments: {len(df)}")
print(f"Passed: {df['passed'].sum()}")
print(f"Failed: {len(failures)}")
print(f"Success rate: {(df['passed'].sum()/len(df)) * 100:.1f}%\n")

# Show all failures
print("\nAll Failures:")
print("-"*70)
for idx, row in failures.iterrows():
    print(f"{row['problem_id']} | {row['strategy']} | {row['llm']}")

# Group by problem
print("\n\nFailures by Problem:")
print("-"*70)
problem_failures = failures.groupby('problem_id').size().sort_values(ascending=False)
for problem, count in problem_failures.items():
    print(f"{problem}: {count} failures")

# Select 2 different failure cases for detailed analysis
print("\n\nSelecting 2 failures for detailed debugging:")
print("-"*70)

selected_failures = []

# Try to get failures from different problems and strategies
for idx, row in failures.iterrows():
    if len(selected_failures) < 2:
        # Check if we already have a failure from this problem
        if not any(f['problem_id'] == row['problem_id'] for f in selected_failures):
            selected_failures.append(row.to_dict())
        elif len(selected_failures) < 2:
            # If we need more, take from same problem but different strategy
            selected_failures.append(row.to_dict())

# Save selected failures
with open('results/selected_failures.json', 'w') as f:
    json.dump(selected_failures, f, indent=2)

for i, failure in enumerate(selected_failures, 1):
    print(f"\n{i}. Problem: {failure['problem_id']}")
    print(f"   Strategy: {failure['strategy']}")
    print(f"   LLM: {failure['llm']}")

print(f"\n✓ Saved to results/selected_failures.json")