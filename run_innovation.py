import json
import time
from llm_interface import LLMInterface
from code_evaluator import extract_python_code, evaluate_code
from innovation_strategy import get_innovative_strategy
from human_eval.data import read_problems

def run_innovation_experiments():
    """
    Test the innovative two-step self-validation strategy
    """
    print("="*70)
    print("PART 3: INNOVATION - TWO-STEP SELF-VALIDATION")
    print("="*70)
    
    # Load problems
    with open('selected_problems.json', 'r') as f:
        problems = json.load(f)
    
    # Initialize LLM
    llm = LLMInterface()
    
    # Get innovative strategy
    strategy = get_innovative_strategy()
    
    print(f"\nNovel Strategy: {strategy['name']}")
    print(f"Description: {strategy['description']}")
    print("="*70)
    
    # LLMs to test
    llm_names = ["claude", "gemini"]
    
    results = []
    detailed_results = []
    
    total = len(problems) * len(llm_names)
    count = 0
    
    for problem_id, problem_data in problems.items():
        problem_prompt = problem_data['prompt']
        entry_point = problem_data['entry_point']
        
        print(f"\nProblem: {problem_id}")
        
        for llm_name in llm_names:
            count += 1
            print(f"  [{count}/{total}] {llm_name}...", end=" ")
            
            try:
                # STEP 1: Initial generation with requirements
                step1_prompt = strategy['step1_template'].format(
                    problem_prompt=problem_prompt
                )
                
                initial_response = llm.generate_code(llm_name, step1_prompt)
                initial_code = extract_python_code(initial_response, entry_point)
                
                # Evaluate initial code
                initial_eval = evaluate_code(problem_id, initial_code)
                initial_pass = initial_eval.get("pass@1", 0.0)
                
                time.sleep(1)
                
                # STEP 2: Self-validation and refinement
                step2_prompt = strategy['step2_template'].format(
                    problem_prompt=problem_prompt,
                    generated_code=initial_code
                )
                
                refined_response = llm.generate_code(llm_name, step2_prompt)
                refined_code = extract_python_code(refined_response, entry_point)
                
                # Evaluate refined code
                refined_eval = evaluate_code(problem_id, refined_code)
                refined_pass = refined_eval.get("pass@1", 0.0)
                
                # Store results
                improvement = refined_pass - initial_pass
                
                results.append({
                    "problem_id": problem_id,
                    "llm": llm_name,
                    "initial_pass": initial_pass,
                    "refined_pass": refined_pass,
                    "improvement": improvement,
                    "passed": refined_pass > 0
                })
                
                detailed_results.append({
                    "problem_id": problem_id,
                    "llm": llm_name,
                    "step1_prompt": step1_prompt,
                    "initial_code": initial_code,
                    "initial_pass": initial_pass,
                    "step2_prompt": step2_prompt,
                    "refined_code": refined_code,
                    "refined_pass": refined_pass,
                    "improvement": improvement
                })
                
                status = "PASS" if refined_pass > 0 else "FAIL"
                if improvement > 0:
                    print(f"{status} (improved: {initial_pass:.1f}→{refined_pass:.1f})")
                else:
                    print(f"{status} ({refined_pass:.1f})")
                
            except Exception as e:
                print(f"ERROR: {e}")
                results.append({
                    "problem_id": problem_id,
                    "llm": llm_name,
                    "initial_pass": 0.0,
                    "refined_pass": 0.0,
                    "improvement": 0.0,
                    "passed": False
                })
    
    # Save results
    with open('results/part3_innovation_results.json', 'w') as f:
        json.dump(detailed_results, f, indent=2)
    
    # Analysis
    print("\n" + "="*70)
    print("INNOVATION RESULTS")
    print("="*70)
    
    total_tests = len(results)
    passed = sum(1 for r in results if r['passed'])
    improvements = [r for r in results if r['improvement'] > 0]
    
    print(f"\nOverall Performance:")
    print(f"  Pass rate: {passed}/{total_tests} ({(passed/total_tests)*100:.1f}%)")
    
    print(f"\nBy LLM:")
    for llm_name in llm_names:
        llm_results = [r for r in results if r['llm'] == llm_name]
        llm_passed = sum(1 for r in llm_results if r['passed'])
        llm_improved = sum(1 for r in llm_results if r['improvement'] > 0)
        print(f"  {llm_name}:")
        print(f"    Pass rate: {llm_passed}/{len(llm_results)} ({(llm_passed/len(llm_results))*100:.1f}%)")
        print(f"    Improved from Step 1: {llm_improved}/{len(llm_results)}")
    
    print(f"\nStep 2 Improvements:")
    print(f"  Cases that improved: {len(improvements)}/{total_tests}")
    if improvements:
        avg_improvement = sum(r['improvement'] for r in improvements) / len(improvements)
        print(f"  Average improvement: {avg_improvement:.3f}")
    
    # Compare to baseline from Part 1
    print(f"\n" + "="*70)
    print("COMPARISON TO PART 1 BASELINE")
    print("="*70)
    
    import pandas as pd
    part1_df = pd.read_csv("results/part1_results.csv")
    baseline_df = part1_df[part1_df['strategy'] == 'Baseline']
    
    for llm_name in llm_names:
        baseline_pass_rate = baseline_df[baseline_df['llm'] == llm_name]['passed'].mean() * 100
        innovation_results = [r for r in results if r['llm'] == llm_name]
        innovation_pass_rate = (sum(1 for r in innovation_results if r['passed']) / len(innovation_results)) * 100
        
        print(f"\n{llm_name.upper()}:")
        print(f"  Part 1 Baseline: {baseline_pass_rate:.1f}%")
        print(f"  Part 3 Innovation: {innovation_pass_rate:.1f}%")
        print(f"  Difference: {innovation_pass_rate - baseline_pass_rate:+.1f}%")
    
    print(f"\nResults saved to: results/part3_innovation_results.json")
    
    return results

if __name__ == "__main__":
    run_innovation_experiments()