import json
from human_eval.data import read_problems

# Load failures
with open('results/selected_failures.json', 'r') as f:
    failures = json.load(f)

# Load generated code
with open('generated_code/all_generated_code.json', 'r') as f:
    generated_codes = json.load(f)

# Load problems
problems = read_problems()

print("="*70)
print("DETAILED FAILURE ANALYSIS")
print("="*70)

for i, failure in enumerate(failures, 1):
    problem_id = failure['problem_id']
    strategy = failure['strategy']
    llm = failure['llm']
    
    print(f"\n{'='*70}")
    print(f"FAILURE {i}")
    print(f"{'='*70}")
    print(f"Problem: {problem_id}")
    print(f"Strategy: {strategy}")
    print(f"LLM: {llm}")
    
    # Get problem details
    problem = problems[problem_id]
    print(f"\nProblem Description:")
    print("-"*70)
    print(problem['prompt'])
    
    # Get generated code
    strategy_key = strategy.lower().replace('-', '_').replace(' ', '_')
    code_key = f"{problem_id}_{strategy_key}_{llm}"
    
    if code_key in generated_codes:
        code_data = generated_codes[code_key]
        
        print(f"\nGenerated Code:")
        print("-"*70)
        print(code_data['extracted_code'])
        
        print(f"\nPrompt Used:")
        print("-"*70)
        print(code_data['prompt'][:300] + "...")
    else:
        print(f"\nCode key not found: {code_key}")
        print("Available keys:", list(generated_codes.keys())[:5])