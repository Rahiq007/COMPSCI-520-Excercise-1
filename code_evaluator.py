import re
import json
import os
import tempfile
import subprocess
import sys

def extract_python_code(llm_response, entry_point):
    """
    Extract Python function from LLM response
    """
    if not llm_response:
        return ""
    
    # Try to find code between ```python and ```
    pattern = r"```python\s*\n(.*?)```"
    matches = re.findall(pattern, llm_response, re.DOTALL | re.IGNORECASE)
    
    if matches:
        code = matches[0].strip()
        # Make sure it contains the function
        if f"def {entry_point}" in code:
            return code
    
    # Try to find code between ``` and ```
    pattern = r"```\s*\n(.*?)```"
    matches = re.findall(pattern, llm_response, re.DOTALL)
    
    if matches:
        code = matches[0].strip()
        if f"def {entry_point}" in code:
            return code
    
    # Try to extract function definition directly
    # Look for the function and everything after it
    pattern = rf"(def {entry_point}\([^)]*\).*?)(?=\n(?:def |class |\Z))"
    matches = re.findall(pattern, llm_response, re.DOTALL)
    
    if matches:
        return matches[0].strip()
    
    # Last resort: if the response contains the function name, return it
    if f"def {entry_point}" in llm_response:
        # Find the start of the function
        start_idx = llm_response.find(f"def {entry_point}")
        if start_idx != -1:
            # Take everything from the function definition onwards
            return llm_response[start_idx:].strip()
    
    return ""

def simple_test_code(problem_id, generated_code):
    """
    Simple syntax check
    """
    try:
        compile(generated_code, '<string>', 'exec')
        return True
    except SyntaxError:
        return False

def evaluate_code(problem_id, generated_code, timeout=5.0):
    """
    Evaluate generated code by running it with test cases
    """
    if not generated_code or generated_code.strip() == "":
        return {"pass@1": 0.0, "result": "empty_code"}
    
    # First check if code compiles
    if not simple_test_code(problem_id, generated_code):
        return {"pass@1": 0.0, "result": "syntax_error"}
    
    # Load the problem to get test cases
    from human_eval.data import read_problems
    problems = read_problems()
    
    if problem_id not in problems:
        return {"pass@1": 0.0, "result": "problem_not_found"}
    
    problem = problems[problem_id]
    
    # Create test file
    test_code = f"""
{generated_code}

# Test cases
{problem['test']}

check({problem['entry_point']})
"""
    
    # Try to execute the test
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(test_code)
            temp_file = f.name
        
        # Run the test
        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        # Clean up
        os.remove(temp_file)
        
        # Check if it passed (no output means success in HumanEval)
        if result.returncode == 0:
            return {"pass@1": 1.0, "result": "passed"}
        else:
            return {"pass@1": 0.0, "result": f"failed: {result.stderr[:100]}"}
    
    except subprocess.TimeoutExpired:
        return {"pass@1": 0.0, "result": "timeout"}
    except Exception as e:
        return {"pass@1": 0.0, "result": f"error: {str(e)[:100]}"}