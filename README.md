# COMPSCI 520 Excercise -1 

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **Course Assignment**: Exploring Code Generation with Large Language Models

## 📌 Overview

This project systematically evaluates how different prompting strategies influence code generation quality across two leading LLM families: **Claude (Anthropic)** and **Gemini (Google)**.

We investigate baseline performance, debugging approaches, and novel prompting innovations to improve reliability, with a focus on:
- **Completeness** of generated code
- **Correctness** against test cases
- **Robustness** across different problem types

---

## 📊 Results Summary

| Metric | Part 1 | Part 2 (Debugging) | Part 3 (Innovation) |
|--------|--------|-------------------|---------------------|
| **Overall Pass Rate** | 88.8% | 100% | 100% |
| **Claude Performance** | 77.5% | – | **100%** (+50% vs baseline) |
| **Gemini Performance** | 100% | – | 100% |

---

## 🔑 Key Findings

- ✅ **Gemini** consistently outperformed Claude in baseline tests (100% vs 50%)
- 📈 **Advanced prompting** significantly boosts Claude's performance (Baseline 50% → CoT/Stepwise 90%)
- ⚠️ **Primary failure mode**: Missing import statements in generated code
- 🎯 **Innovation validated**: Our Two-Step Self-Validation strategy achieved **100% pass rate** for both LLMs

---

## 📂 Project Structure

```
llm-code-generation-assignment/
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
├── generated_code/               # Generated code samples
│   └── all_generated_code.json
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🧪 Strategies Tested

### Part 1: Standard Prompting Strategies

| Strategy | Description |
|----------|-------------|
| **Baseline** | Direct problem statement |
| **Chain-of-Thought (CoT)** | Step-by-step reasoning |
| **Stepwise-CoT** | Explicit breakdown of solution steps |
| **Self-Planning** | Pre-implementation planning |

### Part 3: Novel Innovation

**Two-Step Self-Validation**:
1. Generate code with explicit requirements (imports, edge cases, correctness)
2. Self-validate and refine using a structured checklist

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- API keys for Claude (Anthropic) and Gemini (Google)

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

4. **Set up API keys**
   
   Create a `.env` file in the project root:
   ```env
   ANTHROPIC_API_KEY=your_anthropic_key_here
   GOOGLE_API_KEY=your_google_key_here
   ```

---

## 🚀 Usage

### Run All Experiments

```bash
# Part 1: Baseline and standard strategies
python run_experiments.py

# Part 2: Debugging failures
python debug_failures.py

# Part 3: Innovation strategy
python run_innovation.py
```

### View Results

Results are saved in the `results/` directory:
- `part1_results.csv` - Baseline and standard strategy performance
- `part2_debugging_results.json` - Debugging analysis
- `part3_innovation_results.json` - Innovation strategy results

---

## 📚 Dataset

- **Source**: [HumanEval](https://github.com/openai/human-eval) (10 selected problems)
- **Focus**: Data structures and algorithms
- **Evaluation Metric**: pass@1 (test case pass rate)

---

## 💡 Innovation: Two-Step Self-Validation

Our novel strategy directly addresses the most common LLM failure mode—**omitted import statements**.

### How It Works

**Step 1: Generate with Requirements**
- Generate code with an explicit requirements checklist
- Include: imports, edge cases, completeness

**Step 2: Self-Validation**
- LLM validates its own output via a structured checklist
- Corrects issues if needed

### Results

✅ **100% pass rate** for both LLMs  
✅ Claude improvement: **+50%** over baseline

---

## 📈 Performance Comparison

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

---

## 👤 Author

**Rahiq Majeed**

- GitHub: [Rahiq007](https://github.com/Rahiq007)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- HumanEval dataset by OpenAI
- Anthropic Claude API
- Google Gemini API

---
