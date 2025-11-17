"""
Exercise 3: Coverage Comparison Analysis
Compares Exercise 2 (baseline + improved) vs Exercise 3 (spec-guided tests)
"""

import json

# ============================================================================
# COVERAGE DATA
# ============================================================================

# Exercise 2 Data (from your previous work)
EXERCISE_2_DATA = {
    'HumanEval_54': {
        'baseline': {
            'stmt_coverage': 31.0,
            'branch_coverage': 31.0,
            'tests_passed': 1
        },
        'final': {
            'stmt_coverage': 31.0,
            'branch_coverage': 31.0,
            'tests_passed': 10,  # After all iterations
            'iterations': 3
        }
    },
    'HumanEval_2': {
        'baseline': {
            'stmt_coverage': 44.0,
            'branch_coverage': 44.0,
            'tests_passed': 1
        },
        'final': {
            'stmt_coverage': 56.0,
            'branch_coverage': 56.0,
            'tests_passed': 16,  # After all iterations
            'iterations': 3
        }
    }
}

# Exercise 3 Data (spec-guided tests)
EXERCISE_3_DATA = {
    'HumanEval_54': {
        'spec_guided': {
            'stmt_coverage': 31.0,
            'branch_coverage': 31.0,
            'tests_passed': 12,
            'specifications': 5,
            'accuracy': 100.0
        }
    },
    'HumanEval_2': {
        'spec_guided': {
            'stmt_coverage': 44.0,
            'branch_coverage': 44.0,
            'tests_passed': 12,
            'specifications': 5,
            'accuracy': 100.0
        }
    }
}

# ============================================================================
# COMPARISON FUNCTIONS
# ============================================================================

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*80)
    print(text.center(80))
    print("="*80)

def print_problem_comparison(problem_id):
    """Print detailed comparison for a problem"""
    ex2 = EXERCISE_2_DATA[problem_id]
    ex3 = EXERCISE_3_DATA[problem_id]
    
    print(f"\n{'='*60}")
    print(f"PROBLEM: {problem_id}")
    print('='*60)
    
    # Statement Coverage Comparison
    print("\n📊 STATEMENT COVERAGE:")
    print(f"{'Approach':<30} {'Coverage':<15} {'Tests':<10}")
    print('-'*60)
    print(f"{'Exercise 2 - Baseline':<30} {ex2['baseline']['stmt_coverage']:>6.1f}%{'':<8} {ex2['baseline']['tests_passed']:>3}")
    print(f"{'Exercise 2 - Final (Iterative)':<30} {ex2['final']['stmt_coverage']:>6.1f}%{'':<8} {ex2['final']['tests_passed']:>3}")
    print(f"{'Exercise 3 - Spec-Guided':<30} {ex3['spec_guided']['stmt_coverage']:>6.1f}%{'':<8} {ex3['spec_guided']['tests_passed']:>3}")
    
    # Change Analysis
    ex2_improvement = ex2['final']['stmt_coverage'] - ex2['baseline']['stmt_coverage']
    ex3_vs_baseline = ex3['spec_guided']['stmt_coverage'] - ex2['baseline']['stmt_coverage']
    ex3_vs_final = ex3['spec_guided']['stmt_coverage'] - ex2['final']['stmt_coverage']
    
    print(f"\n📈 IMPROVEMENTS:")
    print(f"  Exercise 2 Improvement: {ex2_improvement:+.1f}% (from baseline to final)")
    print(f"  Exercise 3 vs Ex2 Baseline: {ex3_vs_baseline:+.1f}%")
    print(f"  Exercise 3 vs Ex2 Final: {ex3_vs_final:+.1f}%")
    
    # Branch Coverage
    print(f"\n🌿 BRANCH COVERAGE:")
    print(f"{'Approach':<30} {'Branch Coverage':<15}")
    print('-'*60)
    print(f"{'Exercise 2 - Baseline':<30} {ex2['baseline']['branch_coverage']:>6.1f}%")
    print(f"{'Exercise 2 - Final':<30} {ex2['final']['branch_coverage']:>6.1f}%")
    print(f"{'Exercise 3 - Spec-Guided':<30} {ex3['spec_guided']['branch_coverage']:>6.1f}%")

def print_summary_table():
    """Print summary table for report"""
    print_header("SUMMARY TABLE FOR REPORT")
    
    print("\n| Problem | Old Stmt % | New Stmt % | Old Branch % | New Branch % |")
    print("|---------|------------|------------|--------------|--------------|")
    
    for problem_id in ['HumanEval_54', 'HumanEval_2']:
        ex2_final = EXERCISE_2_DATA[problem_id]['final']
        ex3_spec = EXERCISE_3_DATA[problem_id]['spec_guided']
        
        print(f"| {problem_id:<15} | {ex2_final['stmt_coverage']:>9.1f}% | {ex3_spec['stmt_coverage']:>9.1f}% | {ex2_final['branch_coverage']:>11.1f}% | {ex3_spec['branch_coverage']:>11.1f}% |")

def print_insights():
    """Print case-specific insights"""
    print_header("CASE-SPECIFIC INSIGHTS")
    
    print("\n" + "─"*80)
    print("HumanEval_54: same_chars")
    print("─"*80)
    print("""
✅ Coverage Status: 31% (Exercise 2 Final) → 31% (Exercise 3 Spec-Guided)

📊 Analysis:
- NO CHANGE in coverage between Exercise 2 and Exercise 3
- The core function (line 17) was already fully covered in Exercise 2 baseline
- Both Exercise 2 and Exercise 3 achieve 31% due to uncovered `if __name__` block

🔍 Why No Improvement:
1. The function is very simple: `return set(s0) == set(s1)` (single line)
2. No branches to test - it's a pure function with no conditionals
3. Specifications correctly captured all behavior (100% accuracy)
4. Missing coverage is from lines 22-31 (main block) which pytest cannot reach

💡 Conclusion:
Specification-driven approach validated existing comprehensive test coverage.
The function has maximum achievable coverage for the actual implementation.
""")
    
    print("\n" + "─"*80)
    print("HumanEval_2: truncate_number")
    print("─"*80)
    print("""
📊 Coverage Status: 56% (Exercise 2 Final) → 44% (Exercise 3 Spec-Guided)

📉 Analysis:
- DECREASE of 12% compared to Exercise 2 final
- Exercise 3 matches Exercise 2 baseline (44%)
- Missing critical error handling branch

🔍 Why Spec-Guided Tests Missed Coverage:
1. Problem description states: "Given a POSITIVE floating point number"
2. Specifications were generated based on this description
3. NO specification created for negative number handling
4. Exercise 2 discovered this branch through iterative coverage-driven testing
5. Line 12 `raise ValueError("Number must be non-negative")` NOT tested

📖 Key Differences in Approaches:

Exercise 2 (Coverage-Driven):
  ✅ Iteratively analyzed missing lines
  ✅ Generated tests for uncovered branches
  ✅ Discovered error handling requirements
  ✅ Final: 56% coverage

Exercise 3 (Specification-Driven):
  ✅ Based on problem description only
  ✅ Generated formal specifications for "positive numbers"
  ❌ Did not infer negative number error handling
  ⚠️  Final: 44% coverage (matches baseline)

💡 Conclusion:
Specification-driven testing is limited by the completeness of the problem
description. When the description doesn't mention edge cases or error handling,
specifications won't cover them. Coverage-driven iterative testing (Exercise 2)
is more effective at discovering these hidden requirements.
""")

def print_overall_analysis():
    """Print overall analysis"""
    print_header("OVERALL ANALYSIS: EXERCISE 2 vs EXERCISE 3")
    
    print("""
🎯 Key Findings:

1. SPECIFICATION ACCURACY:
   ✅ 100% accuracy (10/10 specifications correct)
   ✅ All specifications followed formal rules (no self-reference, no side effects)
   ✅ Specifications correctly captured stated requirements

2. COVERAGE COMPARISON:
   Problem          Ex2 Final    Ex3 Spec-Guided    Difference
   HumanEval_54        31%            31%              0%
   HumanEval_2         56%            44%            -12%

3. TEST COMPREHENSIVENESS:
   - Exercise 2: 26 total tests (after iterations)
   - Exercise 3: 24 tests (12 per problem)
   - Both approaches generated thorough test suites

4. ADVANTAGES OF SPECIFICATION-DRIVEN (Exercise 3):
   ✅ Formal verification of correctness
   ✅ Captures intended behavior explicitly
   ✅ Creates documentation of requirements
   ✅ Tests are derived from specifications, not coverage gaps
   ✅ Better for verifying correctness than coverage

5. ADVANTAGES OF COVERAGE-DRIVEN (Exercise 2):
   ✅ Discovers hidden edge cases and error handling
   ✅ Iteratively improves until comprehensive
   ✅ Not limited by problem description completeness
   ✅ Better for maximizing code coverage

6. LIMITATION DISCOVERED:
   ⚠️  Specification-driven testing is only as complete as the problem description
   ⚠️  Implicit requirements (like error handling) may be missed
   ⚠️  Exercise 2's coverage-driven approach caught error handling that Exercise 3 missed

📖 Conclusion:
Both approaches are valuable:
- Specification-driven: Better for CORRECTNESS verification
- Coverage-driven: Better for COMPLETENESS discovery

Ideal approach: Combine both - use specifications for core behavior,
then use coverage analysis to discover missing edge cases.
""")

def save_results_json():
    """Save results to JSON file"""
    results = {
        'exercise2': EXERCISE_2_DATA,
        'exercise3': EXERCISE_3_DATA,
        'comparison': {
            'HumanEval_54': {
                'ex2_improvement': 0.0,
                'ex3_vs_ex2_final': 0.0,
                'conclusion': 'No change - function already fully covered'
            },
            'HumanEval_2': {
                'ex2_improvement': 12.0,
                'ex3_vs_ex2_final': -12.0,
                'conclusion': 'Spec-guided missed error handling branch'
            }
        }
    }
    
    with open('coverage_comparison_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n✅ Results saved to: coverage_comparison_results.json")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print_header("EXERCISE 3: COVERAGE COMPARISON ANALYSIS")
    
    # Compare each problem
    print_problem_comparison('HumanEval_54')
    print_problem_comparison('HumanEval_2')
    
    # Print summary table
    print_summary_table()
    
    # Print insights
    print_insights()
    
    # Print overall analysis
    print_overall_analysis()
    
    # Save results
    save_results_json()
    
    print("\n" + "="*80)
    print("✅ ANALYSIS COMPLETE!")
    print("="*80)
    print("\n📝 Use the summary table and insights above in your report")
    print("📊 All data saved to coverage_comparison_results.json")
    print("="*80)