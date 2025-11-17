# Exercise 3 Project Structure

## Directory Layout

```
exercise3/
  |
  +-- README.md                              (Main documentation)
  +-- exercise3_workflow.py                  (Interactive guide)
  +-- .gitignore                             (Git ignore rules)
  |
  +-- PHASE 1: Problem Description Extraction
  +-- extract_problem_descriptions.py
  +-- problem_descriptions.json
  |
  +-- PHASE 2: Specification Generation (Part 1)
  +-- part1_generate_spec_prompts.py
  +-- prompts/
      +-- spec_generation_HumanEval_54.txt
      +-- spec_generation_HumanEval_2.txt
  +-- specifications/
      +-- HumanEval_54_generated.py         (LLM output)
      +-- HumanEval_54_corrected.py         (After review)
      +-- HumanEval_2_generated.py
      +-- HumanEval_2_corrected.py
  |
  +-- PHASE 3: Specification Evaluation
  +-- spec_evaluation_template.py
  |
  +-- PHASE 4: Test Generation (Part 2)
  +-- part2_generate_test_prompts.py
  +-- prompts/
      +-- test_generation_HumanEval_54.txt
      +-- test_generation_HumanEval_2.txt
  +-- tests/
      +-- test_HumanEval_54_spec_guided.py
      +-- test_HumanEval_2_spec_guided.py
  |
  +-- PHASE 5: Coverage Comparison
  +-- part2_compare_coverage.py
  +-- coverage_comparison_results.json
  |
  +-- solutions/                             (From Exercise 2)
      +-- HumanEval_54.py
      +-- HumanEval_2.py
  |
  +-- coverage_reports/                      (Generated reports)
      +-- README.md
      +-- *.html (gitignored)
```

## Workflow

1. Setup: Run python exercise3_setup.py (DONE!)
2. Extract: Run python extract_problem_descriptions.py
3. Generate Specs: Run python part1_generate_spec_prompts.py
4. Use LLM: Copy prompts to LLM, get specifications
5. Evaluate: Edit spec_evaluation_template.py
6. Generate Tests: Run python part2_generate_test_prompts.py
7. Use LLM: Copy prompts to LLM, get test cases
8. Compare: Run python part2_compare_coverage.py

## Files to Submit

### GitHub:
- All Python files
- All prompts
- All specifications (generated and corrected)
- All test files
- Solutions
- README.md

### PDF Report:
- Part 1: Prompts, accuracy, corrections
- Part 2: Test prompts, coverage table, insights