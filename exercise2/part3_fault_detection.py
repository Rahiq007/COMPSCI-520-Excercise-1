"""
Part 3: Fault Detection Verification
This script tests buggy versions against improved test suites
"""
import subprocess
import sys
import shutil
import os

def backup_original(problem_name):
    """Backup the original solution"""
    original = f"solutions/{problem_name}.py"
    backup = f"solutions/{problem_name}_original_backup.py"
    shutil.copy(original, backup)
    print(f"✓ Backed up {original} to {backup}")

def restore_original(problem_name):
    """Restore the original solution"""
    backup = f"solutions/{problem_name}_original_backup.py"
    original = f"solutions/{problem_name}.py"
    if os.path.exists(backup):
        shutil.copy(backup, original)
        print(f"✓ Restored {original} from backup")

def inject_bug(problem_name, buggy_file):
    """Replace solution with buggy version"""
    original = f"solutions/{problem_name}.py"
    shutil.copy(buggy_file, original)
    print(f"✓ Injected bug from {buggy_file} into {original}")

def run_tests(problem_name):
    """Run tests and return results"""
    test_file = f"tests/test_{problem_name}.py"
    cmd = [
        "pytest",
        test_file,
        "-v",
        "--tb=short"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def analyze_fault_detection(problem_name, bug_description):
    """Analyze fault detection for a problem"""
    
    print("\n" + "="*80)
    print(f"FAULT DETECTION ANALYSIS: {problem_name}")
    print("="*80)
    
    # Step 1: Backup original
    backup_original(problem_name)
    
    # Step 2: Run tests on original (should pass)
    print(f"\nStep 1: Testing ORIGINAL solution...")
    result_original = run_tests(problem_name)
    original_passed = result_original.returncode == 0
    
    if original_passed:
        print("✓ All tests PASS on original solution (expected)")
    else:
        print("✗ Tests FAILED on original solution (unexpected!)")
        print(result_original.stdout)
    
    # Step 3: Inject bug
    print(f"\nStep 2: Injecting bug...")
    print(f"Bug Description: {bug_description}")
    buggy_file = f"{problem_name}_buggy.py"
    inject_bug(problem_name, buggy_file)
    
    # Step 4: Run tests on buggy version
    print(f"\nStep 3: Testing BUGGY solution...")
    result_buggy = run_tests(problem_name)
    buggy_failed = result_buggy.returncode != 0
    
    # Parse which tests failed
    failed_tests = []
    for line in result_buggy.stdout.split('\n'):
        if 'FAILED' in line:
            # Extract test name
            parts = line.split('::')
            if len(parts) >= 2:
                test_name = parts[1].split(' ')[0]
                failed_tests.append(test_name)
    
    print("\n" + "-"*80)
    print("RESULTS:")
    print("-"*80)
    
    if buggy_failed:
        print("✓ Tests CAUGHT the bug! (expected)")
        print(f"\nNumber of tests that failed: {len(failed_tests)}")
        print("\nTests that caught the bug:")
        for test in failed_tests:
            print(f"  - {test}")
    else:
        print("✗ Tests did NOT catch the bug (problem!)")
    
    # Step 5: Restore original
    print(f"\nStep 4: Restoring original solution...")
    restore_original(problem_name)
    
    # Step 6: Verify restoration
    result_restored = run_tests(problem_name)
    if result_restored.returncode == 0:
        print("✓ Original solution restored and tests pass")
    
    print("="*80)
    
    return {
        'problem': problem_name,
        'bug_description': bug_description,
        'bug_caught': buggy_failed,
        'tests_that_caught': failed_tests,
        'total_failed': len(failed_tests)
    }

def main():
    """Run fault detection for both problems"""
    
    print("="*80)
    print("PART 3: FAULT DETECTION VERIFICATION")
    print("="*80)
    print("\nThis script will:")
    print("1. Test original solutions (should pass)")
    print("2. Inject realistic bugs")
    print("3. Test buggy solutions (should fail)")
    print("4. Identify which tests caught the bugs")
    print("5. Restore original solutions")
    
    results = []
    
    # Test HumanEval_54
    result_54 = analyze_fault_detection(
        'HumanEval_54',
        'Changed == to >= in set comparison (superset instead of equality)'
    )
    results.append(result_54)
    
    # Test HumanEval_2
    result_2 = analyze_fault_detection(
        'HumanEval_2',
        'Changed condition from < 0 to <= 0 (off-by-one error, rejects zero)'
    )
    results.append(result_2)
    
    # Final summary
    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    
    for result in results:
        print(f"\n{result['problem']}:")
        print(f"  Bug: {result['bug_description']}")
        print(f"  Bug Caught: {'✓ YES' if result['bug_caught'] else '✗ NO'}")
        print(f"  Tests Failed: {result['total_failed']}")
    
    print("\n" + "="*80)
    print("CONCLUSION:")
    print("="*80)
    
    all_caught = all(r['bug_caught'] for r in results)
    if all_caught:
        print("✓ All bugs were successfully caught by the improved test suites!")
        print("✓ This demonstrates that increased coverage correlates with better fault detection.")
    else:
        print("⚠ Some bugs were not caught. More test cases may be needed.")
    
    print("="*80)

if __name__ == "__main__":
    main()