"""
Part 1: Specification Evaluation
Evaluate and correct LLM-generated specifications

Instructions:
1. Review each specification below
2. Mark as 'Correct' or 'Incorrect'
3. For incorrect ones, provide issue and correction
4. Run this script to see accuracy rate
"""

# ============================================================================
# PROBLEM: HumanEval_54 - same_chars
# ============================================================================

HUMANEVAL_54_GENERATED_SPECS = """
# Specification 1: Core property - result equals set equality
assert res == (set(s0) == set(s1))  # Result must be True iff both strings have identical character sets

# Specification 2: Result is boolean type
assert isinstance(res, bool)  # Result must be a boolean value

# Specification 3: Symmetric property
assert res == (set(s1) == set(s0))  # Function is symmetric - order of arguments doesn't matter

# Specification 4: Empty string handling
assert (len(s0) == 0 and len(s1) == 0) <= (res == True)  # Two empty strings should return True

# Specification 5: Character count independence
assert res == (len(set(s0) & set(s1)) == len(set(s0)) and len(set(s0) & set(s1)) == len(set(s1)))  # Intersection of character sets equals both individual sets
"""

HUMANEVAL_54_EVALUATION = [
    {
        'assertion': 'assert res == (set(s0) == set(s1))',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert isinstance(res, bool)',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert res == (set(s1) == set(s0))',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert (len(s0) == 0 and len(s1) == 0) <= (res == True)',
        'status': 'Correct',
        'issue': None,
        'corrected': None,
        'note': 'Uses <= for logical implication in Python, which is valid'
    },
    {
        'assertion': 'assert res == (len(set(s0) & set(s1)) == len(set(s0)) and len(set(s0) & set(s1)) == len(set(s1)))',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    }
]

# ============================================================================
# PROBLEM: HumanEval_2 - truncate_number
# ============================================================================

HUMANEVAL_2_GENERATED_SPECS = """
# Specification 1: Result is the decimal part
assert res == (number - int(number))  # Result equals the number minus its integer part

# Specification 2: Result range constraint
assert 0 <= res < 1  # Decimal part must be between 0 (inclusive) and 1 (exclusive)

# Specification 3: Reconstruction property
assert number == int(number) + res  # Original number can be reconstructed from integer part and result

# Specification 4: Non-negativity
assert res >= 0  # Decimal part is always non-negative

# Specification 5: Integer input handling
assert (number == int(number)) <= (res == 0)  # If input is an integer, result should be 0
"""

HUMANEVAL_2_EVALUATION = [
    {
        'assertion': 'assert res == (number - int(number))',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert 0 <= res < 1',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert number == int(number) + res',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert res >= 0',
        'status': 'Correct',
        'issue': None,
        'corrected': None
    },
    {
        'assertion': 'assert (number == int(number)) <= (res == 0)',
        'status': 'Correct',
        'issue': None,
        'corrected': None,
        'note': 'Uses <= for logical implication, which is valid'
    }
]

# ============================================================================
# ACCURACY CALCULATION
# ============================================================================

def calculate_accuracy(evaluations):
    """Calculate accuracy rate for specifications"""
    if not evaluations:
        return 0.0, 0, 0
    
    correct = sum(1 for e in evaluations if e['status'] == 'Correct')
    total = len(evaluations)
    accuracy = (correct / total) * 100
    
    return accuracy, correct, total

def print_evaluation_summary():
    """Print summary of evaluation"""
    print("="*80)
    print("SPECIFICATION EVALUATION SUMMARY")
    print("="*80)
    
    # HumanEval_54
    print(f"\n{'='*60}")
    print("HumanEval_54: same_chars")
    print('='*60)
    acc_54, correct_54, total_54 = calculate_accuracy(HUMANEVAL_54_EVALUATION)
    print(f"Total Specifications: {total_54}")
    print(f"Correct: {correct_54}")
    print(f"Incorrect: {total_54 - correct_54}")
    print(f"Accuracy Rate: {acc_54:.1f}%")
    
    # HumanEval_2
    print(f"\n{'='*60}")
    print("HumanEval_2: truncate_number")
    print('='*60)
    acc_2, correct_2, total_2 = calculate_accuracy(HUMANEVAL_2_EVALUATION)
    print(f"Total Specifications: {total_2}")
    print(f"Correct: {correct_2}")
    print(f"Incorrect: {total_2 - correct_2}")
    print(f"Accuracy Rate: {acc_2:.1f}%")
    
    # Overall
    print(f"\n{'='*60}")
    print("OVERALL")
    print('='*60)
    total_all = total_54 + total_2
    correct_all = correct_54 + correct_2
    acc_all = (correct_all / total_all * 100) if total_all > 0 else 0
    print(f"Total Specifications: {total_all}")
    print(f"Correct: {correct_all}")
    print(f"Incorrect: {total_all - correct_all}")
    print(f"Overall Accuracy Rate: {acc_all:.1f}%")
    print("="*80)

def print_corrections():
    """Print table of incorrect assertions and corrections"""
    print("\n" + "="*80)
    print("INCORRECT ASSERTIONS AND CORRECTIONS")
    print("="*80)
    
    all_incorrect = []
    
    # Collect HumanEval_54 incorrect
    for e in HUMANEVAL_54_EVALUATION:
        if e['status'] == 'Incorrect':
            all_incorrect.append(('HumanEval_54', e))
    
    # Collect HumanEval_2 incorrect
    for e in HUMANEVAL_2_EVALUATION:
        if e['status'] == 'Incorrect':
            all_incorrect.append(('HumanEval_2', e))
    
    if not all_incorrect:
        print("\n✅ No incorrect specifications found!")
        print("   All generated specifications are logically correct!")
    else:
        for problem, e in all_incorrect:
            print(f"\n{'─'*80}")
            print(f"Problem: {problem}")
            print(f"Original: {e['assertion']}")
            print(f"Issue: {e['issue']}")
            print(f"Corrected: {e['corrected']}")
    
    print("="*80)

def print_detailed_review():
    """Print detailed review of each specification"""
    print("\n" + "="*80)
    print("DETAILED SPECIFICATION REVIEW")
    print("="*80)
    
    print("\n" + "─"*80)
    print("HumanEval_54: same_chars")
    print("─"*80)
    for i, e in enumerate(HUMANEVAL_54_EVALUATION, 1):
        status_icon = "✅" if e['status'] == 'Correct' else "❌"
        print(f"\n{status_icon} Specification {i}: {e['status']}")
        print(f"   {e['assertion']}")
        if e.get('note'):
            print(f"   Note: {e['note']}")
        if e.get('issue'):
            print(f"   Issue: {e['issue']}")
        if e.get('corrected'):
            print(f"   Corrected: {e['corrected']}")
    
    print("\n" + "─"*80)
    print("HumanEval_2: truncate_number")
    print("─"*80)
    for i, e in enumerate(HUMANEVAL_2_EVALUATION, 1):
        status_icon = "✅" if e['status'] == 'Correct' else "❌"
        print(f"\n{status_icon} Specification {i}: {e['status']}")
        print(f"   {e['assertion']}")
        if e.get('note'):
            print(f"   Note: {e['note']}")
        if e.get('issue'):
            print(f"   Issue: {e['issue']}")
        if e.get('corrected'):
            print(f"   Corrected: {e['corrected']}")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    print_evaluation_summary()
    print_corrections()
    print_detailed_review()
    
    print("\n" + "="*80)
    print("NEXT STEPS:")
    print("="*80)
    print("1. Review the evaluation above")
    print("2. If you disagree with any evaluation, edit this file")
    print("3. Save the corrected specifications to specifications/ directory")
    print("4. Run part2_generate_test_prompts.py to create test generation prompts")
    print("="*80)