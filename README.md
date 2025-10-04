LLM Code Generation: Prompting, Debugging, and Innovation

Course Assignment · Exploring Code Generation with Large Language Models

📌 Overview

This project systematically evaluates how different prompting strategies influence code generation quality across two leading LLM families: Claude (Anthropic) and Gemini (Google).

We investigate baseline performance, debugging approaches, and novel prompting innovations to improve reliability, with a focus on completeness, correctness, and robustness of generated code.

📊 Results Summary
Metric	Part 1	Part 2 (Debugging)	Part 3 (Innovation)
Overall Pass Rate	88.8%	100%	100%
Claude Performance	77.5%	–	100% (+50% vs baseline)
Gemini Performance	100%	–	100%
🔑 Key Findings

Gemini consistently outperformed Claude in baseline tests (100% vs 50%).

Advanced prompting significantly boosts Claude’s performance (Baseline 50% → CoT/Stepwise 90%).

Primary failure mode: Missing import statements in generated code.

Innovation validated: Our Two-Step Self-Validation strategy achieved 100% pass rate for both LLMs.

📂 Project Structure
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
    └── all_generated_code.json

🧪 Strategies Tested
Part 1: Standard Prompting Strategies

Baseline: Direct problem statement.

Chain-of-Thought (CoT): Step-by-step reasoning.

Stepwise-CoT: Explicit breakdown of solution steps.

Self-Planning: Pre-implementation planning.

Part 3: Novel Innovation

Two-Step Self-Validation:

Generate code with explicit requirements (imports, edge cases, correctness).

Self-validate and refine using a checklist.

⚙️ How to Run

Install dependencies

pip install -r requirements.txt


Set up API keys in .env

ANTHROPIC_API_KEY=your_key
GOOGLE_API_KEY=your_key


Run experiments

python run_experiments.py   # Part 1
python debug_failures.py    # Part 2
python run_innovation.py    # Part 3

📚 Dataset

Source: HumanEval (10 selected problems)

Focus: Data structures and algorithms

Evaluation Metric: pass@1 (test case pass rate)

🚀 Innovation: Two-Step Self-Validation

Our novel strategy directly addresses the most common LLM failure mode—omitted import statements:

Step 1: Generate code with an explicit requirements checklist (imports, edge cases, completeness).

Step 2: LLM validates its own output via a structured checklist, correcting issues if needed.

✅ Result: 100% pass rate for both LLMs, with Claude improving by +50% over baseline.

👤 Author

Rahiq Majeed

📄 License

This project is licensed under the MIT License.