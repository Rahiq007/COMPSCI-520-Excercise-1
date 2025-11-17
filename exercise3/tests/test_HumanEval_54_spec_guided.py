"""
Spec-Guided Test Cases for HumanEval_54: same_chars
Generated based on formal specifications
Tests verify that two strings have the same set of characters
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))
from HumanEval_54 import same_chars


def test_same_chars_identical_strings():
    """Test specification 1: Core property - strings with same characters"""
    # Same strings should return True
    assert same_chars('abc', 'abc') == True
    assert same_chars('hello', 'hello') == True


def test_same_chars_different_order():
    """Test specification 1 & 3: Character sets equal regardless of order (symmetry)"""
    # Different order, same characters
    assert same_chars('abc', 'cba') == True
    assert same_chars('abcd', 'dcba') == True
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True


def test_same_chars_different_frequency():
    """Test specification 5: Character count independence - frequency doesn't matter"""
    # Same characters but different frequencies
    assert same_chars('aaa', 'a') == True
    assert same_chars('abcd', 'aabbccdd') == True
    assert same_chars('abcd', 'dddddddabc') == True


def test_same_chars_different_characters():
    """Test specification 1: Strings with different character sets"""
    # Different characters should return False
    assert same_chars('abc', 'def') == False
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'abce') == False


def test_same_chars_subset():
    """Test specification 1 & 5: One string has subset of other's characters"""
    # One string missing characters from the other
    assert same_chars('abc', 'abcd') == False
    assert same_chars('abcd', 'abc') == False
    assert same_chars('abcd', 'dddddddabce') == False


def test_same_chars_empty_strings():
    """Test specification 4: Empty string handling"""
    # Both empty should return True
    assert same_chars('', '') == True
    # One empty, one not should return False
    assert same_chars('', 'a') == False
    assert same_chars('a', '') == False


def test_same_chars_single_character():
    """Test specification 1: Single character strings"""
    assert same_chars('a', 'a') == True
    assert same_chars('a', 'b') == False
    assert same_chars('x', 'x') == True


def test_same_chars_symmetric_property():
    """Test specification 3: Function is symmetric - order of arguments doesn't matter"""
    # f(s0, s1) should equal f(s1, s0)
    assert same_chars('abc', 'cba') == same_chars('cba', 'abc')
    assert same_chars('hello', 'olleh') == same_chars('olleh', 'hello')
    assert same_chars('test', 'xyz') == same_chars('xyz', 'test')


def test_same_chars_return_type():
    """Test specification 2: Result is boolean type"""
    # Result should always be a boolean
    result1 = same_chars('abc', 'abc')
    assert isinstance(result1, bool)
    
    result2 = same_chars('abc', 'def')
    assert isinstance(result2, bool)
    
    result3 = same_chars('', '')
    assert isinstance(result3, bool)


def test_same_chars_special_characters():
    """Test specification 1: Strings with special characters"""
    assert same_chars('!@#', '#@!') == True
    assert same_chars('a!b@c#', '#c@b!a') == True
    assert same_chars('123', '321') == True
    assert same_chars('abc', 'abc!') == False


def test_same_chars_whitespace():
    """Test specification 1: Strings with whitespace"""
    assert same_chars('a b c', 'c b a') == True
    assert same_chars('hello world', 'world hello') == True
    assert same_chars('  ', '  ') == True
    assert same_chars('abc', 'abc ') == False


def test_same_chars_case_sensitive():
    """Test specification 1: Case sensitivity"""
    # Should be case sensitive (different cases = different characters)
    assert same_chars('ABC', 'abc') == False
    assert same_chars('Hello', 'hello') == False
    assert same_chars('ABC', 'ABC') == True