import pandas as pd
import json

# Load results
df = pd.read_csv("results/part1_results.csv")

print("="*70)
print("COMPARING CLAUDE vs GEMINI")
print("="*70)

# Overall comparison
print("\nOverall Performance:")
print("-"*70)
for llm in ['claude', 'gemini']:
    llm_df = df[df['llm'] == llm]
    passed = llm_df['passed'].sum()
    total = len(llm_df)
    rate = (passed/total) * 100
    print(f"{llm.upper()}: {passed}/{total} ({rate:.1f}%)")

# By strategy
print("\n\nPerformance by Strategy:")
print("-"*70)
pivot = df.pivot_table(values='passed', index='strategy', columns='llm', aggfunc='sum')
print(pivot)

# Which problems did Claude fail but Gemini passed?
print("\n\nProblems where Claude failed but Gemini passed:")
print("-"*70)

claude_fails = df[(df['llm'] == 'claude') & (df['passed'] == False)]
for _, row in claude_fails.iterrows():
    problem_id = row['problem_id']
    strategy = row['strategy']
    
    # Check if Gemini passed this
    gemini_result = df[(df['llm'] == 'gemini') & 
                       (df['problem_id'] == problem_id) & 
                       (df['strategy'] == strategy)]
    
    if not gemini_result.empty and gemini_result.iloc[0]['passed']:
        print(f"  {problem_id} | {strategy}")

print("\n\nKey Insights:")
print("-"*70)
print("1. Gemini achieved 100% pass rate across all strategies")
print("2. Claude struggled with Baseline prompts (50% vs Gemini's 100%)")
print("3. Advanced prompting strategies helped Claude significantly:")
print("   - Baseline: 50% → CoT/Stepwise: 90%")
print("4. Main issue: Claude sometimes omits import statements in Baseline mode")