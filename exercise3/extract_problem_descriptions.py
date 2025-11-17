"""
Extract problem descriptions from Exercise 2 solutions
This script reads the solution files and extracts:
1. Function signature
2. Problem description from docstring
"""

import os
import ast
import json

def extract_problem_info(solution_file):
    """Extract function signature and docstring from a Python file"""
    with open(solution_file, 'r') as f:
        content = f.read()
    
    # Parse the Python file
    tree = ast.parse(content)
    
    # Find the first function definition
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Get function name
            func_name = node.name
            
            # Get function signature
            args = []
            for arg in node.args.args:
                arg_name = arg.arg
                # Try to get type annotation if available
                if arg.annotation:
                    arg_type = ast.unparse(arg.annotation)
                    args.append(f"{arg_name}: {arg_type}")
                else:
                    args.append(arg_name)
            
            # Get return type if available
            return_type = ""
            if node.returns:
                return_type = f" -> {ast.unparse(node.returns)}"
            
            signature = f"def {func_name}({', '.join(args)}){return_type}"
            
            # Get docstring
            docstring = ast.get_docstring(node) or "No description available"
            
            return {
                'function_name': func_name,
                'signature': signature,
                'description': docstring.strip()
            }
    
    return None

def main():
    # Problems we're focusing on
    problems = ['HumanEval_54', 'HumanEval_2']
    
    # Path to Exercise 2 solutions (adjust this path)
    base_path = input("Enter the path to your exercise2/solutions directory: ").strip()
    
    if not os.path.exists(base_path):
        print(f"❌ Directory not found: {base_path}")
        return
    
    problem_info = {}
    
    for problem in problems:
        solution_file = os.path.join(base_path, f"{problem}.py")
        
        if not os.path.exists(solution_file):
            print(f"❌ File not found: {solution_file}")
            continue
        
        print(f"\n{'='*60}")
        print(f"Extracting: {problem}")
        print('='*60)
        
        info = extract_problem_info(solution_file)
        
        if info:
            problem_info[problem] = info
            
            print(f"\n📝 Function: {info['function_name']}")
            print(f"📋 Signature: {info['signature']}")
            print(f"\n📖 Description:")
            print(info['description'])
        else:
            print(f"⚠️  Could not extract info from {problem}")
    
    # Save to JSON file
    output_file = 'problem_descriptions.json'
    with open(output_file, 'w') as f:
        json.dump(problem_info, f, indent=2)
    
    print(f"\n✅ Problem descriptions saved to: {output_file}")
    print(f"\n{'='*60}")
    print("Next steps:")
    print("1. Review the problem descriptions above")
    print("2. Run part1_generate_spec_prompts.py to create specification prompts")
    print('='*60)

if __name__ == "__main__":
    main()