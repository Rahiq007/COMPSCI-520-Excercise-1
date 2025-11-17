# COMPSCI 520 - Software Engineering Course Assignments

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **Course Assignments**: Exploring LLM-Powered Software Engineering

## 📌 Repository Overview

This repository contains comprehensive assignments exploring modern software engineering practices with Large Language Models (LLMs), covering:

1. **Exercise 1**: Code Generation with LLMs
2. **Exercise 2**: Automated Testing & Coverage Analysis
3. **Exercise 3**: Specification-Guided Test Improvement

---

# 📝 Exercise 1: Code Generation with LLMs

## Overview

Systematic evaluation of how different prompting strategies influence code generation quality across **Claude (Anthropic)** and **Gemini (Google)**.

### 📊 Results Summary

| Metric | Part 1 | Part 2 (Debugging) | Part 3 (Innovation) |
|--------|--------|-------------------|---------------------|
| **Overall Pass Rate** | 88.8% | 100% | 100% |
| **Claude Performance** | 77.5% | – | **100%** (+50% vs baseline) |
| **Gemini Performance** | 100% | – | 100% |

### 🔑 Key Findings

- ✅ **Gemini** consistently outperformed Claude in baseline tests (100% vs 50%)
- 📈 **Advanced prompting** significantly boosts Claude's performance (Baseline 50% → CoT/Stepwise 90%)
- ⚠️ **Primary failure mode**: Missing import statements in generated code
- 🎯 **Innovation validated**: Two-Step Self-Validation strategy achieved **100% pass rate** for both LLMs

### 🧪 Strategies Tested

| Strategy | Description |
|----------|-------------|
| **Baseline** | Direct problem statement |
| **Chain-of-Thought (CoT)** | Step-by-step reasoning |
| **Stepwise-CoT** | Explicit breakdown of solution steps |
| **Self-Planning** | Pre-implementation planning |
| **Two-Step Self-Validation** | Generate + validate with checklist (Innovation) |

### 📂 Exercise 1 Structure

```
exercise1/
├── prompting_strategies.py       # Strategy definitions
├── llm_interface.py              # LLM API interfaces
├── code_evaluator.py             # Code extraction and testing
├── run_experiments.py            # Part 1: Baseline & standard strategies
├── debug_failures.py             # Part 2: Debugging failures
├── innovation_strategy.py        # Part 3: Novel strategy definition
├── run_innovation.py             # Part 3: Runner for innovation
├── results/                      # Experimental results
│   ├── part1_results.csv
│   ├── part2_debugging_results.json
│   └── part3_innovation_results.json
└── generated_code/               # Generated code samples
```

---

# 🧪 Exercise 2: Automated Testing & Coverage Analysis

## Overview

Comprehensive study of automated testing, coverage analysis, and fault detection using LLM-assisted test generation. This assignment explores the correlation between code coverage and bug detection capability.

### 📊 Results Summary

| Problem | Baseline Coverage | Final Coverage | Improvement | Tests Generated | Bugs Caught |
|---------|------------------|----------------|-------------|-----------------|-------------|
| **HumanEval_54** | 31% | 31% | 0% (Converged) | 12 tests | ✓ 6 failures |
| **HumanEval_2** | 44% | 56% | +12% | 16 tests | ✓ 4 failures |
| **Overall** | 67% | 67% | – | 10 problems | 100% detection |

### 🔑 Key Findings

#### Part 1: Baseline Coverage Analysis
- ✅ **Initial Coverage**: 67% overall (173 statements, 84 branches)
- 📊 **Selection Metric**: |%test_passed - %branch_coverage| × %test_passed
- 🎯 **Selected Problems**: HumanEval_54 (31%) and HumanEval_2 (44%) - lowest coverage

#### Part 2: LLM-Assisted Test Generation
- 📈 **Convergence Achieved**: Both problems converged within 2-3 iterations
- 🎯 **HumanEval_2 Improvement**: Critical +12% gain by testing ValueError branch
- ⚙️ **Convergence Criteria**: <3% improvement over 3 consecutive iterations
- 📝 **Minimal Redundancy**: Structured prompts produced targeted, non-duplicate tests

#### Part 3: Fault Detection
- ✅ **100% Bug Detection Rate**: All injected bugs caught by improved test suites
- 🐛 **HumanEval_54 Bug**: Operator change (== to >=) caught by 6 tests
- 🐛 **HumanEval_2 Bug**: Off-by-one error (<= instead of <) caught by 4 tests
- 🔗 **Strong Correlation**: Higher coverage → Better fault detection

### 💡 Key Insights

1. **Branch Coverage > Line Coverage**: Branch metrics more meaningful for fault detection
2. **Edge Cases Critical**: Tests targeting boundaries and error paths most valuable
3. **LLM Effectiveness**: Well-structured prompts produce high-quality, targeted tests
4. **Coverage Convergence**: Functions fully covered when only `if __name__` blocks remain untested

### 📂 Exercise 2 Structure

```
exercise2/
├── solutions/                    # LLM-generated solutions from Exercise 1
│   ├── HumanEval_0.py through HumanEval_54.py
│   └── (10 problems total)
├── tests/                        # Test files (baseline + improved)
│   ├── test_HumanEval_0.py through test_HumanEval_54.py
│   └── (Progressive test improvements)
├── coverage_reports/             # Coverage analysis outputs
│   ├── html/                    # HTML coverage reports
│   ├── coverage.xml             # XML report
│   └── coverage.json            # JSON report
├── prompts/                      # LLM prompts used for test generation
│   ├── HumanEval_54_iteration_1.txt
│   ├── HumanEval_54_iteration_2.txt
│   ├── HumanEval_2_iteration_1.txt
│   ├── HumanEval_2_iteration_2.txt
│   └── HumanEval_2_iteration_3.txt
├── iterations/                   # Iteration tracking data
├── part1_baseline.py            # Part 1: Baseline coverage collection
├── part2_prompts.py             # Part 2: Prompt generation and management
├── part3_fault_detection.py     # Part 3: Bug injection and detection
├── extract_solutions.py         # Extract solutions from Exercise 1
├── create_baseline_tests.py     # Generate baseline test files
├── analyze_missing_coverage.py  # Analyze coverage gaps
├── select_problems.py           # Problem selection using metric
├── HumanEval_54_buggy.py       # Buggy version for fault detection
├── HumanEval_2_buggy.py        # Buggy version for fault detection
└── selected_problems.txt        # Selected problems documentation
```

### 🔬 Testing Strategy

#### Iteration Process
1. **Baseline**: Run existing tests, measure coverage
2. **Iteration 1**: Target critical gaps (error paths, edge cases)
3. **Iteration 2+**: Refine coverage until convergence
4. **Validation**: Inject realistic bugs to verify detection

#### Sample Prompts Used

**HumanEval_2 - Iteration 1 (Critical Branch Coverage)**:
```
Generate comprehensive unit tests for truncate_number function.

CRITICAL: Current tests DO NOT cover the negative number ValueError path.

Generate tests that cover:
1. Negative numbers - test that ValueError is raised (use pytest.raises)
2. Zero (0.0 and 0)
3. Integer values (1.0, 5.0, 10.0)
4. Small decimal values (0.1, 0.001, 0.999)
5. Large numbers (1000.5, 999999.123)
6. Edge cases around floating point precision
```

### 🐛 Bugs Injected & Detected

#### HumanEval_54: Operator Precedence Bug
```python
# Original: set(s0) == set(s1)
# Buggy:    set(s0) >= set(s1)
# Result:   6 tests failed ✓
# Tests:    test_same_chars_baseline, test_same_chars_empty_strings, etc.
```

#### HumanEval_2: Off-by-One Boundary Error
```python
# Original: if number < 0
# Buggy:    if number <= 0
# Result:   4 tests failed ✓
# Tests:    test_truncate_number_zero, test_truncate_number_multiple_zeros
```

### 📈 Coverage Progression

**HumanEval_54 (same_chars)**:
```
Iteration 0:  31% █████████████
Iteration 1:  31% █████████████ (Converged - function fully covered)
Iteration 2:  31% █████████████
```

**HumanEval_2 (truncate_number)**:
```
Iteration 0:  44% ████████████████████
Iteration 1:  56% ██████████████████████████ (+12% - ValueError branch covered)
Iteration 2:  56% ██████████████████████████ (Converged)
Iteration 3:  56% ██████████████████████████
```

---

# 🎯 Exercise 3: Specification-Guided Test Improvement

## Overview

Exploration of how formal specifications automatically generated from natural language problem descriptions can guide test improvement. This assignment compares **specification-driven testing** (Exercise 3) with **coverage-driven testing** (Exercise 2) to understand their complementary strengths.

### 📊 Results Summary

| Problem | Ex2 Final Coverage | Ex3 Spec-Guided | Change | Specifications | Accuracy |
|---------|-------------------|-----------------|--------|----------------|----------|
| **HumanEval_54** | 31% | 31% | 0% | 5 specs | 100% |
| **HumanEval_2** | 56% | 44% | -12% | 5 specs | 100% |
| **Overall** | 43.5% | 37.5% | -6% | 10 specs | **100%** |

### 🔑 Key Findings

#### Part 1: Specification Generation & Evaluation
- ✅ **Perfect Accuracy**: 100% (10/10 specifications logically correct)
- 📝 **Zero Corrections**: All generated specifications followed formal rules
- 🎯 **Rule Compliance**: No self-reference, no side effects, pure logic only
- 📊 **Comprehensive Coverage**: Specifications captured core properties, edge cases, and invariants

#### Part 2: Specification-Guided Test Generation
- 🧪 **24 Tests Generated**: 12 per problem, all passing
- 📋 **HumanEval_54 Result**: No coverage change (31% → 31%) - function already fully covered
- 📉 **HumanEval_2 Result**: Coverage decreased (56% → 44%) - missed implicit error handling
- 🔍 **Critical Discovery**: Specification-driven testing limited by problem description completeness

### 💡 Key Insights

#### Advantages of Specification-Driven Testing (Exercise 3)
- ✅ **Formal Verification**: Explicitly captures intended behavior
- ✅ **Documentation**: Specifications serve as executable requirements
- ✅ **Correctness Focus**: Tests derived from logical properties, not coverage gaps
- ✅ **Systematic Approach**: Structured methodology for test generation

#### Advantages of Coverage-Driven Testing (Exercise 2)
- ✅ **Requirement Discovery**: Uncovers implicit requirements (error handling)
- ✅ **Completeness**: Iteratively improves until comprehensive
- ✅ **Empirical**: Not limited by stated problem description
- ✅ **Gap Detection**: Coverage metrics reveal untested paths

#### The Problem Description Gap

**HumanEval_2 Case Study**:
```python
# Problem states: "Given a POSITIVE floating point number"
# ❌ No mention of: negative number handling, error validation

# Exercise 2 (Coverage-Driven) discovered:
if number < 0:
    raise ValueError("Number must be non-negative")  # 56% coverage

# Exercise 3 (Spec-Driven) missed this because:
# - Specifications based only on "positive numbers"
# - No spec for negative number handling
# - Result: 44% coverage (missed error branch)
```

### 🎯 Comparative Analysis

| Aspect | Exercise 2 (Coverage) | Exercise 3 (Specification) |
|--------|----------------------|---------------------------|
| **Approach** | Analyze gaps → Generate tests | Define specs → Generate tests |
| **Input** | Code + coverage metrics | Natural language description |
| **Strength** | Discovers hidden requirements | Formal correctness verification |
| **Weakness** | May generate redundant tests | Limited by description completeness |
| **Best For** | Maximizing completeness | Verifying stated requirements |
| **Final Coverage** | HE_2: 56% | HE_2: 44% |

### 📂 Exercise 3 Structure

```
exercise3/
├── specifications/               # Formal specifications
│   ├── HumanEval_54_generated_specs.py
│   ├── HumanEval_54_corrected_specs.py
│   ├── HumanEval_2_generated_specs.py
│   └── HumanEval_2_corrected_specs.py
├── tests/                        # Spec-guided test files
│   ├── test_HumanEval_54_spec_guided.py  (12 tests)
│   └── test_HumanEval_2_spec_guided.py   (12 tests)
├── prompts/                      # LLM prompts
│   ├── spec_generation_HumanEval_54.txt
│   ├── spec_generation_HumanEval_2.txt
│   ├── test_generation_HumanEval_54.txt
│   └── test_generation_HumanEval_2.txt
├── solutions/                    # Source code from Exercise 2
│   ├── HumanEval_54.py
│   └── HumanEval_2.py
├── extract_problem_descriptions.py    # Extract problem info
├── part1_generate_spec_prompts.py     # Generate spec prompts
├── spec_evaluation_complete.py        # Evaluate specifications
├── part2_generate_test_prompts_auto.py # Generate test prompts
├── coverage_comparison_analysis.py    # Compare Ex2 vs Ex3
├── coverage_comparison_results.json   # Analysis results
├── problem_descriptions.json          # Extracted problem data
└── README.md                          # Documentation
```

### 📋 Generated Specifications Examples

#### HumanEval_54: same_chars
```python
# Specification 1: Core property - result equals set equality
assert res == (set(s0) == set(s1))

# Specification 2: Result is boolean type
assert isinstance(res, bool)

# Specification 3: Symmetric property
assert res == (set(s1) == set(s0))

# Specification 4: Empty string handling
assert (len(s0) == 0 and len(s1) == 0) <= (res == True)

# Specification 5: Character count independence
assert res == (len(set(s0) & set(s1)) == len(set(s0)) and 
               len(set(s0) & set(s1)) == len(set(s1)))
```

All 5 specifications: ✅ **Correct** (100% accuracy)

#### HumanEval_2: truncate_number
```python
# Specification 1: Result is the decimal part
assert res == (number - int(number))

# Specification 2: Result range constraint
assert 0 <= res < 1

# Specification 3: Reconstruction property
assert number == int(number) + res

# Specification 4: Non-negativity
assert res >= 0

# Specification 5: Integer input handling
assert (number == int(number)) <= (res == 0)
```

All 5 specifications: ✅ **Correct** (100% accuracy)

### 🔬 Specification-Guided Test Examples

#### From Specification to Test
```python
# Specification: assert res == (set(s0) == set(s1))
# Generated Test:
def test_same_chars_different_order():
    """Test specification 1 & 3: Character sets equal regardless of order"""
    assert same_chars('abc', 'cba') == True
    assert same_chars('abcd', 'dcba') == True
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
```

### 📊 Specification Accuracy Breakdown

| Problem | Total Specs | Correct | Incorrect | Accuracy | Issues |
|---------|-------------|---------|-----------|----------|---------|
| HumanEval_54 | 5 | 5 | 0 | 100% | None |
| HumanEval_2 | 5 | 5 | 0 | 100% | None |
| **Overall** | **10** | **10** | **0** | **100%** | **None** |

**Critical Rules Followed**:
- ✅ No self-reference (didn't call function itself)
- ✅ No side effects (no print, I/O, random, timing)
- ✅ No data structure modifications (no append, add, remove)
- ✅ Pure logic and arithmetic only
- ✅ Proper use of `res` variable

### 🎓 Lessons Learned

1. **Complementary Approaches**: Neither specification-driven nor coverage-driven is universally superior
   - **Specification-driven**: Better for **correctness** verification
   - **Coverage-driven**: Better for **completeness** discovery

2. **Problem Description Quality Matters**: Effectiveness of specification-driven testing directly correlates with description completeness

3. **Implicit Requirements Challenge**: Error handling and defensive programming often unstated in formal specifications

4. **Best Practice**: Hybrid approach combining both methods:
   - Start with specification-driven testing for core requirements
   - Follow with coverage analysis to discover gaps
   - Generate additional tests for uncovered branches
   - Update specifications based on discovered requirements

---

## 📚 Technologies & Tools

### Exercise 1
- **LLM APIs**: Anthropic Claude, Google Gemini
- **Testing**: Python unittest framework
- **Dataset**: HumanEval (OpenAI)

### Exercise 2
- **Testing Framework**: pytest
- **Coverage Tools**: pytest-cov, coverage.py
- **Report Formats**: HTML, XML, JSON
- **Languages**: Python 3.12+

### Exercise 3
- **Testing Framework**: pytest, pytest-cov
- **Specification Language**: Python assertions
- **Analysis Tools**: Coverage comparison scripts
- **LLM Integration**: Claude for specification generation
- **Languages**: Python 3.12+

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+ (Exercise 1) / Python 3.12+ (Exercise 2 & 3)
- API keys for Claude (Anthropic) and Gemini (Google) - Exercise 1 only

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rahiq007/COMPSCI-520-Excercise-1
   cd COMPSCI-520-Excercise-1
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys (Exercise 1 only)**
   
   Create a `.env` file in the project root:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_key_here
   GOOGLE_API_KEY=your_google_key_here
   ```

---

## 🚀 Usage

### Exercise 1: Code Generation

```bash
# Part 1: Baseline and standard strategies
python run_experiments.py

# Part 2: Debugging failures
python debug_failures.py

# Part 3: Innovation strategy
python run_innovation.py

# View results
cat results/part1_results.csv
```

### Exercise 2: Testing & Coverage

```bash
# Navigate to exercise 2 directory
cd exercise2/

# Part 1: Baseline coverage analysis
python part1_baseline.py

# View coverage report in browser
open coverage_reports/html/index.html  # macOS
xdg-open coverage_reports/html/index.html  # Linux
start coverage_reports/html/index.html  # Windows

# Part 2: Generate prompts and iterate
python part2_prompts.py

# Run improved tests for specific problem
pytest tests/test_HumanEval_2.py --cov=solutions --cov-branch -v

# Part 3: Fault detection verification
python part3_fault_detection.py
```

### Exercise 3: Specification-Guided Testing

```bash
# Navigate to exercise 3 directory
cd exercise3/

# Part 1: Extract problem descriptions and generate spec prompts
python extract_problem_descriptions.py
python part1_generate_spec_prompts.py

# Generate specifications with LLM (manual step)
# Copy prompts from prompts/ directory to your LLM

# Evaluate generated specifications
python spec_evaluation_complete.py

# Part 2: Generate test prompts from specifications
python part2_generate_test_prompts_auto.py

# Generate tests with LLM (manual step)
# Copy test generation prompts to your LLM

# Run spec-guided tests
pytest tests/test_HumanEval_54_spec_guided.py --cov=solutions --cov-branch -v
pytest tests/test_HumanEval_2_spec_guided.py --cov=solutions --cov-branch -v

# Compare Exercise 2 vs Exercise 3 results
python coverage_comparison_analysis.py
```

### Running All Tests (Exercise 2 & 3)

```bash
# Exercise 2: Run all tests with coverage
cd exercise2/
pytest tests/ --cov=solutions --cov-branch --cov-report=html --cov-report=term-missing -v

# Exercise 3: Run all spec-guided tests
cd exercise3/
pytest tests/ --cov=solutions --cov-branch --cov-report=html -v
```

---

## 📊 Results & Reports

### Exercise 1 Results
- `exercise1/results/part1_results.csv` - Baseline and strategy performance
- `exercise1/results/part2_debugging_results.json` - Debugging analysis
- `exercise1/results/part3_innovation_results.json` - Innovation results

### Exercise 2 Results
- `exercise2/coverage_reports/html/index.html` - Interactive coverage report
- `exercise2/coverage_reports/coverage.xml` - XML coverage data
- `exercise2/selected_problems.txt` - Problem selection justification
- `exercise2/prompts/` - All LLM prompts used

### Exercise 3 Results
- `exercise3/specifications/` - Generated and corrected specifications
- `exercise3/coverage_comparison_results.json` - Ex2 vs Ex3 analysis
- `exercise3/prompts/` - All specification and test generation prompts
- `exercise3/tests/` - Spec-guided test files

---

## 📈 Performance Comparison

### Exercise 1: Prompting Strategies
```
Claude Performance:
├─ Baseline:     50%  ████████████
├─ CoT:          90%  ████████████████████████
├─ Stepwise-CoT: 90%  ████████████████████████
└─ Innovation:  100%  ██████████████████████████

Gemini Performance:
├─ Baseline:    100%  ██████████████████████████
└─ Innovation:  100%  ██████████████████████████
```

### Exercise 2: Coverage Improvement
```
Problem HumanEval_54:
├─ Baseline:     31%  ████████
├─ Iteration 1:  31%  ████████ (Converged)
└─ Iteration 2:  31%  ████████

Problem HumanEval_2:
├─ Baseline:     44%  ███████████
├─ Iteration 1:  56%  ██████████████ (+12%)
├─ Iteration 2:  56%  ██████████████ (Converged)
└─ Iteration 3:  56%  ██████████████
```

### Exercise 3: Specification-Driven vs Coverage-Driven
```
HumanEval_54 Coverage Comparison:
├─ Ex2 (Coverage-Driven):      31%  ████████
└─ Ex3 (Specification-Driven): 31%  ████████ (No change)

HumanEval_2 Coverage Comparison:
├─ Ex2 (Coverage-Driven):      56%  ██████████████
└─ Ex3 (Specification-Driven): 44%  ███████████ (-12%)

Specification Accuracy:
└─ Overall Accuracy:          100%  ██████████████████████████ (10/10 correct)
```

---

## 🔬 Research Methodology

### Exercise 1: Controlled Experiments
1. **Baseline Measurement**: Direct prompting without enhancements
2. **Strategy Variations**: CoT, Stepwise-CoT, Self-Planning
3. **Innovation Testing**: Novel Two-Step Self-Validation approach
4. **Comparative Analysis**: Cross-LLM performance evaluation

### Exercise 2: Iterative Test Improvement
1. **Initial Assessment**: Baseline coverage for 10 problems
2. **Problem Selection**: Metric-based selection of 2 problems
3. **LLM-Assisted Generation**: Structured prompts for test creation
4. **Convergence Monitoring**: Track coverage until <3% improvement
5. **Fault Detection**: Inject realistic bugs to validate effectiveness

### Exercise 3: Specification-First Approach
1. **Problem Extraction**: Extract natural language descriptions and signatures
2. **Specification Generation**: LLM generates formal assertions from descriptions
3. **Manual Evaluation**: Review and correct specifications (100% accuracy achieved)
4. **Test Derivation**: Generate tests from validated specifications
5. **Comparative Analysis**: Compare specification-driven vs coverage-driven results

---

## 📖 Key Learnings

### Exercise 1
- **Prompting Matters**: Strategic prompting can double performance (Claude: 50% → 100%)
- **Self-Validation Works**: Having LLMs check their own output significantly reduces errors
- **Import Statements**: Most common failure mode across all strategies

### Exercise 2
- **Coverage ≠ Quality Alone**: But strong correlation with fault detection exists
- **Branch > Line**: Branch coverage is more meaningful metric
- **Edge Cases Win**: Tests targeting boundaries catch the most bugs
- **LLM Test Generation**: Effective with structured, specific prompts
- **Convergence is Real**: Functions reach coverage plateau when fully tested

### Exercise 3
- **Complementary Approaches**: Specification-driven excels at correctness, coverage-driven at completeness
- **Description Completeness Critical**: Specification quality limited by problem description detail
- **Implicit Requirements**: Error handling often missed in specification-driven approach
- **100% Specification Accuracy**: Possible with clear formal rules and structured prompts
- **Hybrid Strategy Best**: Combine both approaches for optimal testing

### Cross-Exercise Insights
1. **LLM Effectiveness**: LLMs excel when given structured, well-defined tasks
2. **Formal Constraints Help**: Clear rules (Exercise 3) produce better results than open-ended generation
3. **Iteration Improves Quality**: Both coverage-driven (Ex2) and specification refinement (Ex3) benefit from iteration
4. **Multiple Perspectives**: Different testing approaches reveal different quality aspects

---

## 👤 Author

**Rahiq Majeed**

- GitHub: [Rahiq007](https://github.com/Rahiq007)
- Email: [Contact via GitHub]

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **Course**: COMPSCI 520 - Software Engineering
- **Institution**: University of Massachusetts Amherst
- **Dataset**: HumanEval by OpenAI
- **LLM Providers**: Anthropic Claude, Google Gemini
- **Testing Tools**: pytest, pytest-cov, coverage.py

---

## 📚 References

1. Chen, M., et al. (2021). "Evaluating Large Language Models Trained on Code" - HumanEval Dataset
2. Anthropic. (2024). Claude API Documentation
3. Google. (2024). Gemini API Documentation
4. pytest-cov Documentation: https://pytest-cov.readthedocs.io/
5. Meyer, B. (1992). "Applying Design by Contract" - Formal Specifications

---

## 🔗 Related Work

- [HumanEval Dataset](https://github.com/openai/human-eval)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [Design by Contract](https://en.wikipedia.org/wiki/Design_by_contract)

---

## 📝 Citation

If you use this work, please cite:

```bibtex
@misc{majeed2025llmse,
  author = {Majeed, Rahiq},
  title = {COMPSCI 520: LLM-Powered Software Engineering Assignments},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/Rahiq007/COMPSCI-520-Excercise-1}
}
```

---

**Last Updated**: November 2025
