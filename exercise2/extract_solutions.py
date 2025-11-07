import json
import os

# Load innovation results (these have 100% pass rate)
with open('../results/part3_innovation_results.json', 'r') as f:
    innovation_results = json.load(f)

# Create solutions directory
os.makedirs('solutions', exist_ok=True)

print("Extracting solutions from Exercise 1...")

# Get unique problems
problems = {}
for result in innovation_results:
    problem_id = result['problem_id']
    if problem_id not in problems:
        problems[problem_id] = result

# Extract code for each problem
for problem_id, result in problems.items():
    # Use the refined code from innovation (it has 100% pass rate)
    code = result['refined_code']
    
    # Create filename (e.g., HumanEval_0.py)
    filename = problem_id.replace('/', '_') + '.py'
    filepath = os.path.join('solutions', filename)
    
    # Write the code
    with open(filepath, 'w') as f:
        f.write(code)
    
    print(f"✓ Extracted {problem_id} -> {filename}")

print(f"\n✓ Total solutions extracted: {len(problems)}")