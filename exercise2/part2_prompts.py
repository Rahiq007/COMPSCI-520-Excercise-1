"""
Part 2: Guided Test Generation for HumanEval_54 and HumanEval_2
This script provides LLM prompts and manages iterations
"""

# ============================================================================
# ITERATION PLAN
# ============================================================================

ITERATION_PLAN = {
    'HumanEval_54': {
        'baseline': {
            'line_coverage': 30.8,
            'branch_coverage': 31,
            'gaps': [
                'Empty string tests',
                'Single character tests',
                'Special characters',
                'Case sensitivity',
                'Unicode characters'
            ]
        },
        'iterations': [
            {
                'iteration': 1,
                'prompt': """
Generate comprehensive unit tests for the following Python function:

```python
def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)
```

The function checks if two strings have the same set of unique characters.

Current baseline tests cover basic cases. Generate tests that cover:
1. Empty strings (both empty, one empty, one non-empty)
2. Single character strings
3. Strings with repeated characters
4. Special characters and symbols
5. Whitespace handling
6. Case sensitivity (uppercase vs lowercase)

Format the tests as pytest functions that can be added to the existing test file.
Import the function as: from HumanEval_54 import same_chars

Provide only the test functions, no additional explanation.
""",
                'target_coverage': 'Aim for >60% branch coverage'
            },
            {
                'iteration': 2,
                'prompt': """
Based on the current coverage gaps, generate additional edge case tests for same_chars function:

```python
def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)
```

Focus on:
1. Unicode and non-ASCII characters (émojis, accented characters)
2. Numeric strings
3. Mixed alphanumeric with special symbols
4. Very long strings vs short strings with same characters
5. Strings with only whitespace characters

Provide only new test functions that don't duplicate previous tests.
""",
                'target_coverage': 'Aim for >80% branch coverage'
            }
        ]
    },
    
    'HumanEval_2': {
        'baseline': {
            'line_coverage': 44.4,
            'branch_coverage': 44,
            'gaps': [
                'Negative number error handling (CRITICAL - line 12 not tested)',
                'Zero value',
                'Very small decimals',
                'Large numbers',
                'Integer inputs (no decimal part)'
            ]
        },
        'iterations': [
            {
                'iteration': 1,
                'prompt': """
Generate comprehensive unit tests for the following Python function:

```python
def truncate_number(number: float) -> float:
    if number < 0:
        raise ValueError("Function expects a positive floating point number")
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

CRITICAL: Current tests DO NOT cover the negative number ValueError path (line 12).

Generate tests that cover:
1. **Negative numbers** - test that ValueError is raised (use pytest.raises)
2. Zero (0.0 and 0)
3. Integer values (1.0, 5.0, 10.0) - should return 0.0
4. Small decimal values (0.1, 0.001, 0.999)
5. Large numbers (1000.5, 999999.123)
6. Edge cases around floating point precision

Format as pytest functions. Import: from HumanEval_2 import truncate_number
Import pytest for testing exceptions: import pytest

Provide only the test functions, no additional explanation.
""",
                'target_coverage': 'Aim for >80% branch coverage (must test negative case!)'
            },
            {
                'iteration': 2,
                'prompt': """
Based on coverage gaps, generate additional edge case tests for truncate_number:

```python
def truncate_number(number: float) -> float:
    if number < 0:
        raise ValueError("Function expects a positive floating point number")
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

Focus on:
1. Boundary values near zero (0.0000001, 0.9999999)
2. Very large floating point numbers
3. Multiple negative number test cases if not fully covered
4. Float precision edge cases (0.30000000000000004)

Provide only new test functions.
""",
                'target_coverage': 'Aim for >90% branch coverage'
            }
        ]
    }
}

# ============================================================================
# PROMPT GENERATION
# ============================================================================

def print_prompts_for_problem(problem_name):
    """Print all iteration prompts for a problem"""
    
    print(f"\n{'='*80}")
    print(f"TEST GENERATION PROMPTS FOR {problem_name}")
    print(f"{'='*80}\n")
    
    plan = ITERATION_PLAN[problem_name]
    
    print(f"BASELINE COVERAGE:")
    print(f"  Line: {plan['baseline']['line_coverage']}%")
    print(f"  Branch: {plan['baseline']['branch_coverage']}%")
    print(f"\nIDENTIFIED GAPS:")
    for gap in plan['baseline']['gaps']:
        print(f"  - {gap}")
    
    print(f"\n{'-'*80}\n")
    
    for iteration in plan['iterations']:
        print(f"ITERATION {iteration['iteration']}:")
        print(f"Target: {iteration['target_coverage']}")
        print(f"\nPROMPT TO USE:")
        print(f"{'-'*80}")
        print(iteration['prompt'])
        print(f"{'-'*80}\n")
        print(f"Save this prompt for your report!")
        print(f"File: prompts/{problem_name}_iteration_{iteration['iteration']}.txt\n")
        print(f"{'='*80}\n")

def save_prompts_to_files():
    """Save all prompts to files for easy access"""
    
    os.makedirs("prompts", exist_ok=True)
    
    for problem_name, plan in ITERATION_PLAN.items():
        for iteration in plan['iterations']:
            filename = f"prompts/{problem_name}_iteration_{iteration['iteration']}.txt"
            with open(filename, 'w') as f:
                f.write(f"Problem: {problem_name}\n")
                f.write(f"Iteration: {iteration['iteration']}\n")
                f.write(f"Target: {iteration['target_coverage']}\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"PROMPT:\n")
                f.write(f"{'='*80}\n\n")
                f.write(iteration['prompt'])
                f.write(f"\n\n{'='*80}\n")
                f.write(f"USAGE:\n")
                f.write(f"1. Copy this prompt to Claude/ChatGPT\n")
                f.write(f"2. Get generated test code\n")
                f.write(f"3. Add tests to tests/test_{problem_name}.py\n")
                f.write(f"4. Run coverage and record results\n")
    
    print("✓ All prompts saved to prompts/ directory")

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*80)
    print("PART 2: LLM-ASSISTED TEST GENERATION")
    print("="*80)
    
    print("\nThis script provides structured prompts for test generation.")
    print("\nWORKFLOW:")
    print("1. Review prompts for each problem and iteration")
    print("2. Use prompts with LLM (Claude/ChatGPT) to generate tests")
    print("3. Add generated tests to test files")
    print("4. Run coverage after each iteration")
    print("5. Continue until convergence (<3% improvement for 3 iterations)")
    
    # Save prompts to files
    print("\n" + "="*80)
    save_prompts_to_files()
    
    # Print prompts for each problem
    print_prompts_for_problem('HumanEval_54')
    print_prompts_for_problem('HumanEval_2')
    
    print("\n" + "="*80)
    print("NEXT STEPS:")
    print("="*80)
    print("1. Review the prompts above (also saved in prompts/ directory)")
    print("2. Start with HumanEval_54 Iteration 1")
    print("3. Copy the prompt and use it with an LLM")
    print("4. Add generated tests to tests/test_HumanEval_54.py")
    print("5. Run: pytest tests/test_HumanEval_54.py --cov=solutions/HumanEval_54 --cov-branch")
    print("6. Record coverage improvement")
    print("7. Repeat for remaining iterations")
    print("="*80)

if __name__ == "__main__":
    import os
    main()