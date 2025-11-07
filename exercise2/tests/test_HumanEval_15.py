# Baseline tests for HumanEval/15
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from HumanEval_15 import string_sequence



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'


def test_string_sequence_baseline():
    """Baseline test from HumanEval"""
    check(string_sequence)
