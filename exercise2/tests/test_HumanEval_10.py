# Baseline tests for HumanEval/10
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from HumanEval_10 import make_palindrome



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('x') == 'x'
    assert candidate('xyz') == 'xyzyx'
    assert candidate('xyx') == 'xyx'
    assert candidate('jerry') == 'jerryrrej'


def test_make_palindrome_baseline():
    """Baseline test from HumanEval"""
    check(make_palindrome)
