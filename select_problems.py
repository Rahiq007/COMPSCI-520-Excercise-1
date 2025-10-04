import json

# Load all problems
with open('humaneval_problems.json', 'r') as f:
    all_problems = json.load(f)

# Select 10 problems with variety (easy, medium, hard)
# These are good for testing different algorithm types
selected_ids = [
    "HumanEval/0",   # has_close_elements - Array comparison
    "HumanEval/1",   # separate_paren_groups - String parsing
    "HumanEval/2",   # truncate_number - Math
    "HumanEval/10",  # make_palindrome - String manipulation
    "HumanEval/11",  # string_xor - Bitwise operations
    "HumanEval/15",  # string_sequence - String generation
    "HumanEval/20",  # find_closest_elements - Sorting/comparison
    "HumanEval/25",  # factorize - Number theory
    "HumanEval/31",  # is_prime - Algorithm
    "HumanEval/54",  # same_chars - Set operations
]

selected_problems = {pid: all_problems[pid] for pid in selected_ids}

# Save selected problems
with open('selected_problems.json', 'w') as f:
    json.dump(selected_problems, f, indent=2)

print(f"✅ Selected {len(selected_problems)} problems")
print("✅ Saved to selected_problems.json\n")

# Print them for review
for i, (pid, problem) in enumerate(selected_problems.items(), 1):
    print(f"{i}. {pid}")
    print(f"   Function: {problem['entry_point']}")
    print(f"   Preview: {problem['prompt'][:80]}...")
    print(f"   {'-'*70}")