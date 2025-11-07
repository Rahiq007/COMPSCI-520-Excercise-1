import json
import os
from human_eval.data import read_problems

# Load HumanEval problems
problems = read_problems()

# Load our selected problems
with open('../selected_problems.json', 'r') as f:
    selected = json.load(f)

print("Creating baseline test files...")

os.makedirs('tests', exist_ok=True)

for problem_id in selected.keys():
    problem = problems[problem_id]
    
    # Get the test code
    test_code = problem['test']
    entry_point = problem['entry_point']
    
    # Create test filename
    test_filename = f"test_{problem_id.replace('/', '_')}.py"
    test_filepath = os.path.join('tests', test_filename)
    
    # Import the solution
    solution_module = problem_id.replace('/', '_')
    
    # Create pytest test file
    test_content = f"""# Baseline tests for {problem_id}
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from {solution_module} import {entry_point}

{test_code}

def test_{entry_point}_baseline():
    \"\"\"Baseline test from HumanEval\"\"\"
    check({entry_point})
"""
    
    with open(test_filepath, 'w') as f:
        f.write(test_content)
    
    print(f"✓ Created {test_filename}")

print("\n✓ Baseline tests created!")