# Baseline tests for HumanEval/11
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from HumanEval_11 import string_xor



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'


def test_string_xor_baseline():
    """Baseline test from HumanEval"""
    check(string_xor)
