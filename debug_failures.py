import json
import time
from llm_interface import LLMInterface
from code_evaluator import extract_python_code, evaluate_code
from human_eval.data import read_problems

def create_improved_prompts(problem_prompt, failure_analysis):
    """
    Create improved prompts based on failure analysis
    """
    improved_prompts = {
        "explicit_imports": f"""{problem_prompt}

IMPORTANT: Include ALL necessary imports in your solution (typing, etc.).
Make sure the code is complete and can run standalone.

Provide the complete Python implementation.""",

        "with_testing_hint": f"""{problem_prompt}

Requirements:
1. Include all necessary imports (from typing import List, etc.)
2. Handle edge cases (empty inputs, single elements)
3. Make sure the function signature exactly matches the specification
4. Test your logic mentally before providing the solution

Provide the complete Python implementation.""",

        "step_by_step_complete": f"""{problem_prompt}

Let's solve this carefully:
1. First, identify what imports are needed
2. Understand the exact input/output format
3. Consider edge cases
4. Implement the solution with all necessary imports

Provide the COMPLETE Python code including all imports.""",
    }
    
    return improved_prompts

def run_debugging():
    """
    Debug the failures with improved prompts
    """
    print("="*70)
    print("PART 2: DEBUGGING & ITERATIVE IMPROVEMENT")
    print("="*70)
    
    # Load failures
    with open('results/selected_failures.json', 'r') as f:
        failures = json.load(f)
    
    # Load problems
    problems = read_problems()
    
    # Load original generated code
    with open('generated_code/all_generated_code.json', 'r') as f:
        generated_codes = json.load(f)
    
    # Initialize LLM
    llm = LLMInterface()
    
    debugging_results = []
    
    for i, failure in enumerate(failures, 1):
        problem_id = failure['problem_id']
        strategy = failure['strategy']
        llm_name = failure['llm']
        
        print(f"\n{'='*70}")
        print(f"DEBUGGING FAILURE {i}: {problem_id}")
        print(f"Original Strategy: {strategy} | LLM: {llm_name}")
        print(f"{'='*70}")
        
        # Get problem data
        problem = problems[problem_id]
        problem_prompt = problem['prompt']
        entry_point = problem['entry_point']
        
        # Get original failed code
        strategy_key = strategy.lower().replace('-', '_').replace(' ', '_')
        code_key = f"{problem_id}_{strategy_key}_{llm_name}"
        original_code = generated_codes.get(code_key, {}).get('extracted_code', 'Not found')
        
        print(f"\nOriginal Failed Code:")
        print("-"*70)
        print(original_code[:300])
        
        # Analyze why it failed
        print(f"\nFailure Analysis:")
        print("-"*70)
        if 'List' in original_code and 'from typing import List' not in original_code:
            print("Issue: Missing import statement for 'List' from typing")
        if 'def ' in original_code and original_code.count('def ') == 1:
            print("Issue: Code seems incomplete or missing imports")
        
        # Create improved prompts
        improved_prompts = create_improved_prompts(problem_prompt, "missing_imports")
        
        # Test each improved prompt
        for improved_name, improved_prompt in improved_prompts.items():
            print(f"\n  Testing improvement: {improved_name}...")
            
            try:
                # Generate new code
                response = llm.generate_code(llm_name, improved_prompt)
                
                if not response:
                    print(f"    FAILED: No response")
                    continue
                
                new_code = extract_python_code(response, entry_point)
                
                # Evaluate
                eval_results = evaluate_code(problem_id, new_code)
                pass_at_1 = eval_results.get("pass@1", 0.0)
                
                result = {
                    "problem_id": problem_id,
                    "original_strategy": strategy,
                    "improved_strategy": improved_name,
                    "llm": llm_name,
                    "original_passed": False,
                    "improved_passed": pass_at_1 > 0,
                    "improved": pass_at_1 > 0,
                    "original_code": original_code,
                    "improved_code": new_code,
                    "original_prompt": generated_codes.get(code_key, {}).get('prompt', ''),
                    "improved_prompt": improved_prompt
                }
                
                debugging_results.append(result)
                
                status = "FIXED!" if pass_at_1 > 0 else "Still failing"
                print(f"    {status} (pass@1: {pass_at_1})")
                
                if pass_at_1 > 0:
                    print(f"\n    What worked:")
                    if 'from typing import' in new_code and 'from typing import' not in original_code:
                        print(f"      - Added missing imports")
                    print(f"      - Improved prompt: {improved_name}")
                    break  # Stop testing other prompts for this failure if we fixed it
                
                time.sleep(1)
                
            except Exception as e:
                print(f"    ERROR: {e}")
    
    # Save debugging results
    with open('results/part2_debugging_results.json', 'w') as f:
        json.dump(debugging_results, f, indent=2)
    
    print(f"\n{'='*70}")
    print("DEBUGGING COMPLETE!")
    print(f"Results saved to: results/part2_debugging_results.json")
    print(f"{'='*70}")
    
    # Summary
    total_attempts = len(debugging_results)
    fixed = sum(1 for r in debugging_results if r['improved'])
    
    print(f"\nSummary:")
    print(f"  Total debugging attempts: {total_attempts}")
    print(f"  Successfully fixed: {fixed}/{len(failures)} original failures")
    print(f"  Success rate: {(fixed/len(failures)*100):.1f}%")
    
    print(f"\nKey Findings:")
    for result in debugging_results:
        if result['improved']:
            print(f"  - {result['problem_id']}: Fixed with '{result['improved_strategy']}'")
    
    return debugging_results

if __name__ == "__main__":
    run_debugging()