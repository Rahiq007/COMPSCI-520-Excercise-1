"""
Part 2: Generate Test Case Prompts
Creates prompts for LLM to generate test cases based on corrected specifications
"""

import json
import os

def read_specifications(problem_id):
    """Read corrected specifications from file"""
    spec_file = f"specifications/{problem_id}_corrected_specs.py"
    
    if not os.path.exists(spec_file):
        print(f"⚠️  Specification file not found: {spec_file}")
        return None
    
    with open(spec_file, 'r') as f:
        return f.read()

def create_test_generation_prompt(problem_id, function_name, signature, description, specifications):
    """
    Create a prompt for generating test cases from specifications
    """
    
    prompt = f"""You are tasked with generating comprehensive test cases based on formal specifications.

Problem Description:
{description}

Method Signature:
{signature}

Formal Specifications (Corrected and Validated):
```python
{specifications}
```

TASK:
Generate comprehensive test cases that verify each specification above. 

REQUIREMENTS:
1. Create test functions using pytest format
2. Each test should clearly verify one or more specifications
3. Include both positive and negative test cases
4. Label each test with a comment indicating which specification(s) it tests
5. Use descriptive test function names that explain what is being tested
6. Include edge cases and boundary conditions
7. Import the function at the top of the file

TEST FILE STRUCTURE:
```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))
from {problem_id} import {function_name}

def test_{function_name}_<descriptive_name>():
    '''Test specification 1: <which spec this tests>'''
    # Test code here
    result = {function_name}(input_args)
    assert result == expected_output
```

IMPORTANT:
- Generate 8-12 test functions
- Cover all specifications comprehensively
- Include edge cases (empty inputs, None, boundary values, etc.)
- Ensure tests are runnable with pytest
- Each test should be independent and self-contained
- Use clear, descriptive test names

Please generate the complete test file with all imports and test functions now:
"""
    
    return prompt

def main():
    print("="*80)
    print("PART 2: GENERATE TEST CASE PROMPTS FROM SPECIFICATIONS")
    print("="*80)
    
    # Load problem descriptions
    if not os.path.exists('problem_descriptions.json'):
        print("\n❌ Error: problem_descriptions.json not found!")
        return
    
    with open('problem_descriptions.json', 'r') as f:
        problem_info = json.load(f)
    
    os.makedirs('prompts', exist_ok=True)
    
    for problem_id, info in problem_info.items():
        print(f"\n{'='*60}")
        print(f"Problem: {problem_id}")
        print('='*60)
        
        # Read corrected specifications
        specifications = read_specifications(problem_id)
        
        if not specifications:
            print(f"⚠️  Skipping {problem_id} - no corrected specifications found")
            continue
        
        # Generate prompt
        prompt = create_test_generation_prompt(
            problem_id,
            info['function_name'],
            info['signature'],
            info['description'],
            specifications
        )
        
        # Save prompt
        prompt_file = f"prompts/test_generation_{problem_id}.txt"
        with open(prompt_file, 'w') as f:
            f.write(prompt)
        
        print(f"\n✅ Test generation prompt saved to: {prompt_file}")
        print(f"\n📋 PROMPT PREVIEW (first 500 chars):")
        print("-" * 60)
        print(prompt[:500] + "...")
        print("-" * 60)
    
    print(f"\n{'='*80}")
    print("NEXT STEPS:")
    print("="*80)
    print("1. Open prompts/test_generation_HumanEval_54.txt")
    print("2. Copy the prompt and paste it to Claude/GPT")
    print("3. Save the generated test file as tests/test_HumanEval_54_spec_guided.py")
    print("4. Repeat for HumanEval_2")
    print("5. Run part2_compare_coverage.py to compare with Exercise 2")
    print("="*80)

if __name__ == "__main__":
    main()