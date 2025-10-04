def get_innovative_strategy():
    """
    Novel Strategy: Two-Step Self-Validation with Import Verification
    
    Innovation:
    - Step 1: Generate code with explicit requirements checklist
    - Step 2: Ask LLM to validate and fix its own code
    - Focus on completeness (imports, edge cases, syntax)
    - Self-correction loop to catch common mistakes
    
    This strategy addresses the key failure mode discovered in Part 2:
    LLMs (especially Claude) sometimes omit import statements in baseline mode.
    """
    
    step1_template = """{problem_prompt}

Requirements for your solution:
1. Include ALL necessary imports at the top (typing, etc.)
2. Implement the complete function with the exact signature
3. Handle edge cases (empty inputs, single elements, etc.)
4. Ensure the code can run standalone

Provide your complete Python implementation."""
    
    step2_template = """Review and validate this code for the following problem:

PROBLEM:
{problem_prompt}

PROPOSED SOLUTION:
```python
{generated_code}
Validation checklist - check each item:

Are all necessary imports included? (typing.List, etc.)
Does the function signature match the specification exactly?
Are edge cases handled properly?
Will this code run without any errors?
Is the logic correct?

If you find ANY issues, provide the corrected version.
If the code is perfect, return it unchanged.
Provide ONLY the final, validated Python code with all necessary imports."""
    
    return {
        "name": "Two-Step Self-Validation",
        "description": "Generate code with requirements, then validate and self-correct",
        "step1_template": step1_template,
        "step2_template": step2_template,
        "multi_step": True
    }
