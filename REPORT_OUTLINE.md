# Report Outline

## 1. Introduction (1 page)
- Assignment objective
- LLMs used: Claude Sonnet 4.5, Gemini 2.0 Flash
- Dataset: HumanEval (10 problems)
- Evaluation metric: pass@1

## 2. Part 1: Prompt Design & Code Generation (2-3 pages)
- Strategies tested (Baseline, CoT, Stepwise-CoT, Self-Planning)
- Results table (pass rates by strategy and LLM)
- Key finding: Gemini 100%, Claude 77.5%
- Analysis: Why Claude struggled with baseline

## 3. Part 2: Debugging & Iterative Improvement (2 pages)
- 2 failure cases analyzed
- Root cause: Missing import statements
- Improved prompts with explicit import instructions
- Results: 2/2 fixed (100% success)

## 4. Part 3: Innovation (2-3 pages)
- Novel strategy: Two-Step Self-Validation
- Methodology: Generate → Self-critique → Refine
- Results: 100% pass rate for both LLMs
- Claude improvement: +50% vs baseline
- Analysis: Why self-validation works

## 5. Conclusion (1 page)
- Summary of findings
- Best practices for LLM code generation
- Future work

## Appendices
- Selected prompts (original and improved)
- Example generated code
- Full results tables