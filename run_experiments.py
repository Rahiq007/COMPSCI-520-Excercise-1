import json
import pandas as pd
from llm_interface import LLMInterface
from prompting_strategies import get_prompt_strategies, format_prompt
from code_evaluator import extract_python_code, evaluate_code
import os
from datetime import datetime

def run_all_experiments():
    """
    Run experiments for all problems, strategies, and LLMs
    """
    print("="*70)
    print("STARTING LLM CODE GENERATION EXPERIMENTS")
    print("="*70)
    
    # Load selected problems
    with open('selected_problems.json', 'r') as f:
        problems = json.load(f)
    
    # Initialize LLM interface
    print("\nInitializing LLM interfaces...")
    try:
        llm = LLMInterface()
        print("  Claude API: Connected")
        print("  Gemini API: Connected")
    except Exception as e:
        print(f"ERROR: Failed to initialize LLMs: {e}")
        print("Please check your .env file has correct API keys")
        return
    
    # Get strategies
    strategies = get_prompt_strategies()
    
    # LLMs to test
    llm_names = ["claude", "gemini"]
    
    # Results storage
    results = []
    generated_codes = {}
    
    # Create directories
    os.makedirs("results", exist_ok=True)
    os.makedirs("generated_code", exist_ok=True)
    
    total_experiments = len(problems) * len(strategies) * len(llm_names)
    print(f"\nExperiment Configuration:")
    print(f"  Problems: {len(problems)}")
    print(f"  Strategies: {len(strategies)}")
    print(f"  LLMs: {len(llm_names)}")
    print(f"  Total experiments: {total_experiments}")
    print("="*70)
    
    experiment_count = 0
    
    # Run experiments
    for problem_id, problem_data in problems.items():
        problem_prompt = problem_data['prompt']
        entry_point = problem_data['entry_point']
        
        print(f"\n{'='*70}")
        print(f"Problem: {problem_id} - {entry_point}")
        print(f"{'='*70}")
        
        for strategy_name, strategy_data in strategies.items():
            print(f"\nStrategy: {strategy_data['name']}")
            
            # Format prompt with strategy
            formatted_prompt = format_prompt(strategy_name, problem_prompt)
            
            for llm_name in llm_names:
                experiment_count += 1
                print(f"  [{experiment_count}/{total_experiments}] {llm_name}...", end=" ")
                
                try:
                    # Generate code
                    response = llm.generate_code(llm_name, formatted_prompt)
                    
                    if response is None:
                        print("FAILED (no response)")
                        results.append({
                            "problem_id": problem_id,
                            "strategy": strategy_data['name'],
                            "llm": llm_name,
                            "pass@1": 0.0,
                            "passed": False
                        })
                        continue
                    
                    # Extract code
                    code = extract_python_code(response, entry_point)
                    
                    # Save generated code
                    code_key = f"{problem_id}_{strategy_name}_{llm_name}"
                    generated_codes[code_key] = {
                        "problem_id": problem_id,
                        "strategy": strategy_data['name'],
                        "llm": llm_name,
                        "prompt": formatted_prompt,
                        "response": response,
                        "extracted_code": code
                    }
                    
                    # Evaluate code
                    eval_results = evaluate_code(problem_id, code)
                    pass_at_1 = eval_results.get("pass@1", 0.0)
                    
                    # Store results
                    results.append({
                        "problem_id": problem_id,
                        "strategy": strategy_data['name'],
                        "llm": llm_name,
                        "pass@1": pass_at_1,
                        "passed": pass_at_1 > 0
                    })
                    
                    status = "PASS" if pass_at_1 > 0 else "FAIL"
                    print(f"{status} ({pass_at_1:.2f})")
                    
                except Exception as e:
                    print(f"ERROR: {e}")
                    results.append({
                        "problem_id": problem_id,
                        "strategy": strategy_data['name'],
                        "llm": llm_name,
                        "pass@1": 0.0,
                        "passed": False
                    })
    
    # Save all results
    results_df = pd.DataFrame(results)
    results_df.to_csv("results/part1_results.csv", index=False)
    
    with open("generated_code/all_generated_code.json", 'w') as f:
        json.dump(generated_codes, f, indent=2)
    
    print("\n" + "="*70)
    print("EXPERIMENTS COMPLETE!")
    print(f"Results saved to: results/part1_results.csv")
    print(f"Generated code saved to: generated_code/all_generated_code.json")
    print("="*70)
    
    # Print summary
    print_summary(results_df)
    
    return results_df, generated_codes

def print_summary(df):
    """Print summary statistics"""
    print("\nSUMMARY STATISTICS")
    print("="*70)
    
    # Overall pass rate
    overall_pass_rate = df['passed'].mean() * 100
    total_passed = df['passed'].sum()
    total_tests = len(df)
    print(f"\nOverall: {total_passed}/{total_tests} passed ({overall_pass_rate:.1f}%)")
    
    # By LLM
    print("\nBy LLM:")
    for llm in df['llm'].unique():
        llm_df = df[df['llm'] == llm]
        passed = llm_df['passed'].sum()
        total = len(llm_df)
        rate = llm_df['passed'].mean() * 100
        print(f"  {llm}: {passed}/{total} ({rate:.1f}%)")
    
    # By Strategy
    print("\nBy Strategy:")
    for strategy in df['strategy'].unique():
        strat_df = df[df['strategy'] == strategy]
        passed = strat_df['passed'].sum()
        total = len(strat_df)
        rate = strat_df['passed'].mean() * 100
        print(f"  {strategy}: {passed}/{total} ({rate:.1f}%)")
    
    # Pivot table
    print("\nDetailed Breakdown (pass rate %):")
    pivot = df.pivot_table(
        values='passed',
        index='strategy',
        columns='llm',
        aggfunc='mean'
    ) * 100
    print(pivot.round(1))

if __name__ == "__main__":
    run_all_experiments()