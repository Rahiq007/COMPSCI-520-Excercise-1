"""
Part 1: Generate Specification Prompts
Creates prompts for LLM to generate formal specifications as assertions
Following Exercise 3 requirements exactly
"""

import json
import os

def create_spec_prompt(problem_id, function_name, signature, description):
    """
    Create a prompt for generating formal specifications
    Following the exact format from Exercise 3 instructions
    """
    
    prompt = f"""Problem description: {description}

Method signature: {signature}

Please write formal specifications as Python assertions that describe the correct behavior of this method.

CRITICAL RULES:
1. Write specifications as assert statements
2. Let 'res' denote the expected return value of {function_name}
3. Do NOT call '{function_name}()' in your assertions (no self-reference)
4. Do NOT use methods with side effects such as:
   - print(), input(), file operations
   - random number generation (random.random())
   - timing functions (time.time(), datetime.now())
   - data structure modifications (list.append(), dict.update(), set.add())
5. Express relationships using ONLY pure arithmetic and boolean logic

Generate approximately 5 formal specifications that capture key properties of this function.

Format each specification as:
assert <logical_expression>  # Comment explaining what this checks

Example format (do not use this exact assertion, generate appropriate ones for the problem):
assert res == (n % 2 == 0)  # Result must equal "n is divisible by 2"
"""
    
    return prompt

def main():
    # Load problem descriptions
    if not os.path.exists('problem_descriptions.json'):
        print("❌ Error: problem_descriptions.json not found!")
        print("Please run extract_problem_descriptions.py first")
        return
    
    with open('problem_descriptions.json', 'r') as f:
        problem_info = json.load(f)
    
    # Create prompts directory
    os.makedirs('prompts', exist_ok=True)
    
    print("="*80)
    print("GENERATING SPECIFICATION PROMPTS FOR PART 1")
    print("="*80)
    
    for problem_id, info in problem_info.items():
        print(f"\n{'='*60}")
        print(f"Problem: {problem_id}")
        print('='*60)
        
        prompt = create_spec_prompt(
            problem_id,
            info['function_name'],
            info['signature'],
            info['description']
        )
        
        # Save prompt to file
        prompt_file = f"prompts/spec_generation_{problem_id}.txt"
        with open(prompt_file, 'w') as f:
            f.write(prompt)
        
        print(f"✅ Saved to: {prompt_file}")
        print(f"\n📋 PROMPT PREVIEW:")
        print("-" * 60)
        print(prompt)
        print("-" * 60)
    
    print(f"\n{'='*80}")
    print("NEXT STEPS:")
    print("="*80)
    print("1. Review the generated prompts in the 'prompts/' directory")
    print("2. Copy each prompt and paste it to Claude/GPT")
    print("3. Save the LLM responses")
    print("4. Run part1_evaluate_specs.py to evaluate the generated specifications")
    print("="*80)

if __name__ == "__main__":
    main()