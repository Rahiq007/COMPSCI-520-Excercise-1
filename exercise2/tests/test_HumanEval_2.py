import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from HumanEval_2 import truncate_number
import pytest


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


# ============================================================================
# BASELINE TEST (from HumanEval benchmark)
# ============================================================================

def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6


def test_truncate_number_baseline():
    """Baseline test from HumanEval"""
    check(truncate_number)


# ============================================================================
# ITERATION 1 TESTS - Generated to improve coverage
# Focus: Test negative number ValueError and edge cases
# ============================================================================

def test_truncate_number_negative_raises_error():
    """Test that negative numbers raise ValueError - CRITICAL TEST"""
    with pytest.raises(ValueError, match="positive floating point number"):
        truncate_number(-1.5)
    
    with pytest.raises(ValueError, match="positive floating point number"):
        truncate_number(-0.1)
    
    with pytest.raises(ValueError, match="positive floating point number"):
        truncate_number(-100.99)


def test_truncate_number_zero():
    """Test with zero values"""
    assert truncate_number(0.0) == 0.0
    assert truncate_number(0) == 0.0


def test_truncate_number_integer_values():
    """Test with integer values (should return 0.0)"""
    assert truncate_number(1.0) == 0.0
    assert truncate_number(5.0) == 0.0
    assert truncate_number(10.0) == 0.0
    assert truncate_number(100.0) == 0.0


def test_truncate_number_small_decimals():
    """Test with small decimal values"""
    assert abs(truncate_number(0.1) - 0.1) < 1e-9
    assert abs(truncate_number(0.001) - 0.001) < 1e-9
    assert abs(truncate_number(0.999) - 0.999) < 1e-9
    assert abs(truncate_number(0.5) - 0.5) < 1e-9


def test_truncate_number_large_numbers():
    """Test with large numbers"""
    assert abs(truncate_number(1000.5) - 0.5) < 1e-9
    assert abs(truncate_number(999999.123) - 0.123) < 1e-9
    assert abs(truncate_number(1234567.89) - 0.89) < 1e-9


def test_truncate_number_float_precision():
    """Test edge cases around floating point precision"""
    result = truncate_number(2.9999999)
    assert 0.9 < result < 1.0
    
    result = truncate_number(10.0000001)
    assert 0.0 < result < 0.001

def test_truncate_number_boundary_near_zero():
    """Test boundary values very close to zero"""
    assert abs(truncate_number(0.0000001) - 0.0000001) < 1e-9
    assert abs(truncate_number(0.9999999) - 0.9999999) < 1e-9
    assert abs(truncate_number(1.0000001) - 0.0000001) < 1e-6


def test_truncate_number_very_large_floats():
    """Test with very large floating point numbers"""
    assert abs(truncate_number(1e10 + 0.5) - 0.5) < 1e-9
    assert abs(truncate_number(999999999.999) - 0.999) < 1e-6 
    assert truncate_number(1e15) == 0.0


def test_truncate_number_more_negative_cases():
    """Additional negative number tests"""
    with pytest.raises(ValueError):
        truncate_number(-0.0001)
    
    with pytest.raises(ValueError):
        truncate_number(-1000.5)
    
    with pytest.raises(ValueError):
        truncate_number(-999999.999)


def test_truncate_number_precision_edge_cases():
    """Test floating point precision edge cases"""
    # Common floating point precision issue
    result = truncate_number(0.1 + 0.2)  # Often equals 0.30000000000000004
    assert 0.29 < result < 0.31
    
    result = truncate_number(1.1 + 1.2)
    assert 0.29 < result < 0.31


def test_truncate_number_repeating_decimals():
    """Test with repeating decimals"""
    assert abs(truncate_number(1.3333333) - 0.3333333) < 1e-6
    assert abs(truncate_number(2.6666666) - 0.6666666) < 1e-6
    assert abs(truncate_number(5.7777777) - 0.7777777) < 1e-6

def test_truncate_number_extreme_small_values():
    """Test with extremely small decimal values"""
    assert abs(truncate_number(0.00000001) - 0.00000001) < 1e-9
    assert abs(truncate_number(1.00000001) - 0.00000001) < 1e-7


def test_truncate_number_multiple_zeros():
    """Test various forms of zero"""
    assert truncate_number(0) == 0.0
    assert truncate_number(0.0) == 0.0
    assert truncate_number(0.00000) == 0.0


def test_truncate_number_edge_negative_values():
    """Additional negative value tests to ensure error handling"""
    with pytest.raises(ValueError):
        truncate_number(-1e-10)
    
    with pytest.raises(ValueError):
        truncate_number(-1e10)


def test_truncate_number_specific_decimal_patterns():
    """Test specific decimal patterns"""
    assert abs(truncate_number(7.77) - 0.77) < 1e-9
    assert abs(truncate_number(9.99) - 0.99) < 1e-9
    assert abs(truncate_number(100.01) - 0.01) < 1e-9