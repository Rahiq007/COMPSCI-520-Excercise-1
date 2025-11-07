# Complete tests for HumanEval_54
# Baseline test + Iteration 1 tests
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from HumanEval_54 import same_chars


METADATA = {}


# ============================================================================
# BASELINE TEST (from HumanEval benchmark)
# ============================================================================

def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False


def test_same_chars_baseline():
    """Baseline test from HumanEval"""
    check(same_chars)


# ============================================================================
# ITERATION 1 TESTS - Generated to improve coverage
# ============================================================================

def test_same_chars_empty_strings():
    """Test with empty strings"""
    assert same_chars('', '') == True
    assert same_chars('', 'a') == False
    assert same_chars('a', '') == False


def test_same_chars_single_character():
    """Test with single characters"""
    assert same_chars('a', 'a') == True
    assert same_chars('a', 'b') == False
    assert same_chars('x', 'x') == True


def test_same_chars_repeated_characters():
    """Test with repeated characters"""
    assert same_chars('aaa', 'a') == True
    assert same_chars('aaa', 'aa') == True
    assert same_chars('aaabbb', 'ab') == True
    assert same_chars('aaabbb', 'ba') == True
    assert same_chars('aaa', 'bbb') == False


def test_same_chars_special_characters():
    """Test with special characters and symbols"""
    assert same_chars('!@#', '!@#') == True
    assert same_chars('!@#', '#@!') == True
    assert same_chars('abc!', 'cba!') == True
    assert same_chars('!@#', '!@$') == False
    assert same_chars('a-b_c', 'c_b-a') == True


def test_same_chars_whitespace():
    """Test whitespace handling"""
    assert same_chars(' ', ' ') == True
    assert same_chars('a b', 'ba ') == True
    assert same_chars('   ', ' ') == True
    assert same_chars(' a', 'a') == False
    assert same_chars('\t\n', '\n\t') == True


def test_same_chars_case_sensitivity():
    """Test case sensitivity"""
    assert same_chars('abc', 'ABC') == False
    assert same_chars('AbC', 'CbA') == True
    assert same_chars('aA', 'Aa') == True
    assert same_chars('hello', 'HELLO') == False

def test_same_chars_unicode():
    """Test with Unicode and non-ASCII characters"""
    assert same_chars('café', 'éfac') == True
    assert same_chars('café', 'cafe') == False
    assert same_chars('😀😃', '😃😀') == True
    assert same_chars('hello', 'héllo') == False


def test_same_chars_numeric_strings():
    """Test with numeric strings"""
    assert same_chars('123', '321') == True
    assert same_chars('123', '1234') == False
    assert same_chars('000', '0') == True
    assert same_chars('12', '21') == True


def test_same_chars_mixed_alphanumeric():
    """Test with mixed alphanumeric and special symbols"""
    assert same_chars('abc123!@#', '#@!321cba') == True
    assert same_chars('a1b2c3', 'c3b2a1') == True
    assert same_chars('test123', 'test124') == False
    assert same_chars('!@#$%', '%$#@!') == True


def test_same_chars_long_vs_short():
    """Test very long strings vs short strings with same chars"""
    assert same_chars('a' * 1000, 'a') == True
    assert same_chars('abcdefghij' * 100, 'jihgfedcba') == True
    assert same_chars('x' * 999 + 'y', 'xy') == True


def test_same_chars_only_whitespace():
    """Test strings with only whitespace characters"""
    assert same_chars('   ', ' ') == True
    assert same_chars('\t\t\t', '\t') == True
    assert same_chars(' \t\n', '\n\t ') == True
    assert same_chars(' \t', '\n') == False