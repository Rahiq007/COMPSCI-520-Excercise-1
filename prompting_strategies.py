def get_prompt_strategies():
    """
    Define different prompting strategies for code generation
    """
    strategies = {
        "baseline": {
            "name": "Baseline",
            "template": "{problem_prompt}\n\nProvide only the Python function implementation."
        },
        
        "chain_of_thought": {
            "name": "Chain-of-Thought",
            "template": """{problem_prompt}

Let's solve this step by step:
1. First, understand what the problem is asking
2. Think about the approach
3. Consider edge cases
4. Implement the solution

Provide the Python function implementation."""
        },
        
        "stepwise_cot": {
            "name": "Stepwise-CoT",
            "template": """{problem_prompt}

Break down the solution:
Step 1: Analyze input and output requirements
Step 2: Identify the algorithm or data structure needed
Step 3: List edge cases to handle
Step 4: Write pseudocode
Step 5: Implement in Python

Provide the Python function implementation."""
        },
        
        "self_planning": {
            "name": "Self-Planning",
            "template": """{problem_prompt}

Before writing code, create a plan:
- What is the input format?
- What is the expected output?
- What algorithm should be used?
- What are the edge cases?
- What is the time complexity?

Then implement the function in Python based on your plan."""
        },
    }
    
    return strategies

def format_prompt(strategy_name, problem_prompt):
    """Format a prompt using the given strategy"""
    strategies = get_prompt_strategies()
    template = strategies[strategy_name]["template"]
    return template.format(problem_prompt=problem_prompt)