"""
Problem Selection Script for Part 2
Calculates: |%test_passed - %branch_coverage| × %test_passed
"""

# Coverage data from Part 1 results
problems = {
    'HumanEval_0': {'line': 63.0, 'branch': 63, 'tests_passed': 100},
    'HumanEval_1': {'line': 89.7, 'branch': 90, 'tests_passed': 100},
    'HumanEval_2': {'line': 44.4, 'branch': 44, 'tests_passed': 100},
    'HumanEval_10': {'line': 60.7, 'branch': 61, 'tests_passed': 100},
    'HumanEval_11': {'line': 61.1, 'branch': 61, 'tests_passed': 100},
    'HumanEval_15': {'line': 66.7, 'branch': 67, 'tests_passed': 100},
    'HumanEval_20': {'line': 69.4, 'branch': 69, 'tests_passed': 100},
    'HumanEval_25': {'line': 73.0, 'branch': 73, 'tests_passed': 100},
    'HumanEval_31': {'line': 81.5, 'branch': 81, 'tests_passed': 100},
    'HumanEval_54': {'line': 30.8, 'branch': 31, 'tests_passed': 100},
}

print("="*80)
print("PROBLEM SELECTION FOR PART 2")
print("="*80)
print(f"\nMetric: |%test_passed - %branch_coverage| × %test_passed\n")
print(f"{'Problem':<15} {'Tests %':<10} {'Branch %':<12} {'Metric Score':<15} {'Rank'}")
print("-"*80)

# Calculate metric for each problem
results = []
for problem, data in problems.items():
    tests_passed = data['tests_passed']
    branch_cov = data['branch']
    
    # Calculate metric
    metric = abs(tests_passed - branch_cov) * tests_passed
    
    results.append({
        'problem': problem,
        'tests_passed': tests_passed,
        'branch_cov': branch_cov,
        'metric': metric
    })

# Sort by metric (highest first)
results.sort(key=lambda x: x['metric'], reverse=True)

# Print results
for i, result in enumerate(results, 1):
    print(f"{result['problem']:<15} {result['tests_passed']:<10} {result['branch_cov']:<12} {result['metric']:<15.0f} #{i}")

print("-"*80)
print("\n" + "="*80)
print("RECOMMENDED PROBLEMS FOR PART 2:")
print("="*80)
print(f"\n1. {results[0]['problem']} (Metric: {results[0]['metric']:.0f}, Branch Coverage: {results[0]['branch_cov']}%)")
print(f"2. {results[1]['problem']} (Metric: {results[1]['metric']:.0f}, Branch Coverage: {results[1]['branch_cov']}%)")

print("\n" + "="*80)
print("JUSTIFICATION:")
print("="*80)
print(f"These two problems have the highest metric scores, indicating:")
print(f"- Significant gap between test pass rate and branch coverage")
print(f"- Most room for improvement through additional test cases")
print(f"- Good candidates for LLM-assisted test generation")
print("="*80)

# Save to file for report
with open('selected_problems.txt', 'w') as f:
    f.write("SELECTED PROBLEMS FOR PART 2\n")
    f.write("="*80 + "\n\n")
    f.write(f"Problem 1: {results[0]['problem']}\n")
    f.write(f"  - Current Branch Coverage: {results[0]['branch_cov']}%\n")
    f.write(f"  - Selection Metric Score: {results[0]['metric']:.0f}\n\n")
    f.write(f"Problem 2: {results[1]['problem']}\n")
    f.write(f"  - Current Branch Coverage: {results[1]['branch_cov']}%\n")
    f.write(f"  - Selection Metric Score: {results[1]['metric']:.0f}\n\n")
    f.write(f"Selection Metric: |%test_passed - %branch_coverage| × %test_passed\n")
    f.write(f"All tests passed (100%), so metric = |100 - branch%| × 100\n")

print("\n✓ Selection saved to 'selected_problems.txt'")