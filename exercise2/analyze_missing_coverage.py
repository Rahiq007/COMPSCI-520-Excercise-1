"""
Part 2: Analyze Missing Coverage for Selected Problems
This script examines HumanEval_54 and HumanEval_2 to identify uncovered code
"""
import json
import os

def analyze_coverage_for_problem(problem_name):
    """Analyze what's missing in coverage for a specific problem"""
    
    print(f"\n{'='*80}")
    print(f"ANALYZING: {problem_name}")
    print(f"{'='*80}\n")
    
    # Read the solution file
    solution_file = f"solutions/{problem_name}.py"
    if os.path.exists(solution_file):
        print(f"Solution Code:")
        print("-"*80)
        with open(solution_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                print(f"{i:3}: {line}", end='')
        print("\n" + "-"*80)
    
    # Read baseline test
    test_file = f"tests/test_{problem_name}.py"
    if os.path.exists(test_file):
        print(f"\nBaseline Test Code:")
        print("-"*80)
        with open(test_file, 'r') as f:
            test_code = f.read()
            print(test_code)
        print("-"*80)
    
    # Parse coverage JSON
    json_path = "coverage_reports/coverage.json"
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Find the file
        for filename, file_data in data['files'].items():
            if problem_name in filename:
                print(f"\nCoverage Details:")
                print("-"*80)
                summary = file_data['summary']
                print(f"Line Coverage: {summary.get('percent_covered', 0):.1f}%")
                print(f"Statements: {summary.get('num_statements', 0)}")
                print(f"Missing Lines: {summary.get('missing_lines', 0)}")
                print(f"Branches: {summary.get('num_branches', 0)}")
                print(f"Partial Branches: {summary.get('num_partial_branches', 0)}")
                
                # Show missing lines
                if 'missing_lines' in file_data:
                    print(f"\nMissing Line Numbers: {file_data['missing_lines']}")
                
                # Show excluded lines
                if 'excluded_lines' in file_data:
                    print(f"Excluded Lines: {file_data['excluded_lines']}")
                
                print("-"*80)
                break

def generate_analysis_summary():
    """Generate summary for both problems"""
    
    print("\n" + "="*80)
    print("PART 2 ANALYSIS SUMMARY")
    print("="*80)
    
    problems = ['HumanEval_54', 'HumanEval_2']
    
    for problem in problems:
        analyze_coverage_for_problem(problem)
    
    print("\n" + "="*80)
    print("NEXT STEPS FOR TEST GENERATION:")
    print("="*80)
    print("""
1. Review the solution code and identify:
   - Conditional branches (if/else)
   - Loop conditions
   - Edge cases
   - Error handling paths

2. Examine baseline tests to understand:
   - What's currently tested
   - What scenarios are missing

3. For each problem, prepare LLM prompts to generate tests for:
   - Uncovered branches
   - Edge cases (empty inputs, boundary values)
   - Error conditions
   - Different data types/formats

4. Run tests iteratively and measure coverage improvement
""")
    print("="*80)

if __name__ == "__main__":
    generate_analysis_summary()