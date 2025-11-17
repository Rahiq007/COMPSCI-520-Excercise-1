"""
Spec-Guided Test Cases for HumanEval_2: truncate_number
Generated based on formal specifications
Tests verify that the function returns the decimal part of a number
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))
from HumanEval_2 import truncate_number


def test_truncate_number_basic_decimal():
    """Test specification 1: Result is the decimal part (number - int(number))"""
    # Basic decimal numbers
    assert truncate_number(3.5) == 0.5
    assert truncate_number(1.25) == 0.25
    assert truncate_number(10.75) == 0.75


def test_truncate_number_range_constraint():
    """Test specification 2: Result must be between 0 (inclusive) and 1 (exclusive)"""
    # All results should be in [0, 1)
    result1 = truncate_number(5.3)
    assert 0 <= result1 < 1
    
    result2 = truncate_number(100.999)
    assert 0 <= result2 < 1
    
    result3 = truncate_number(0.5)
    assert 0 <= result3 < 1


def test_truncate_number_reconstruction():
    """Test specification 3: Original number = int(number) + result"""
    # Can reconstruct original from integer part and decimal part
    number1 = 3.5
    result1 = truncate_number(number1)
    assert abs(number1 - (int(number1) + result1)) < 1e-10
    
    number2 = 15.789
    result2 = truncate_number(number2)
    assert abs(number2 - (int(number2) + result2)) < 1e-10
    
    number3 = 0.123
    result3 = truncate_number(number3)
    assert abs(number3 - (int(number3) + result3)) < 1e-10


def test_truncate_number_non_negativity():
    """Test specification 4: Decimal part is always non-negative"""
    # All results should be >= 0
    assert truncate_number(5.0) >= 0
    assert truncate_number(3.14159) >= 0
    assert truncate_number(100.001) >= 0


def test_truncate_number_integer_input():
    """Test specification 5: Integer input should return 0"""
    # If input is an integer, decimal part is 0
    assert truncate_number(5.0) == 0.0
    assert truncate_number(10.0) == 0.0
    assert truncate_number(100.0) == 0.0
    assert truncate_number(1.0) == 0.0


def test_truncate_number_small_decimals():
    """Test specification 1: Small decimal values"""
    assert abs(truncate_number(0.1) - 0.1) < 1e-10
    assert abs(truncate_number(0.01) - 0.01) < 1e-10
    assert abs(truncate_number(0.001) - 0.001) < 1e-10


def test_truncate_number_large_integers_with_decimals():
    """Test specification 1 & 3: Large numbers with small decimals"""
    assert abs(truncate_number(1000.5) - 0.5) < 1e-10
    assert abs(truncate_number(9999.1) - 0.1) < 1e-10
    assert abs(truncate_number(12345.67) - 0.67) < 1e-10


def test_truncate_number_near_one():
    """Test specification 2: Decimals close to 1 but less than 1"""
    result1 = truncate_number(5.999)
    assert 0 <= result1 < 1
    assert abs(result1 - 0.999) < 1e-10
    
    result2 = truncate_number(10.9999)
    assert 0 <= result2 < 1
    assert abs(result2 - 0.9999) < 1e-10


def test_truncate_number_fractional_only():
    """Test specification 1: Numbers less than 1 (only fractional part)"""
    # When integer part is 0, result equals the input
    assert abs(truncate_number(0.5) - 0.5) < 1e-10
    assert abs(truncate_number(0.75) - 0.75) < 1e-10
    assert abs(truncate_number(0.333) - 0.333) < 1e-10


def test_truncate_number_various_precisions():
    """Test specification 1 & 2: Different decimal precisions"""
    assert abs(truncate_number(2.5) - 0.5) < 1e-10
    assert abs(truncate_number(2.55) - 0.55) < 1e-10
    assert abs(truncate_number(2.555) - 0.555) < 1e-10
    assert abs(truncate_number(2.5555) - 0.5555) < 1e-10


def test_truncate_number_mathematical_constants():
    """Test specification 1 & 3: Common mathematical values"""
    # Pi
    pi_result = truncate_number(3.14159)
    assert abs(pi_result - 0.14159) < 1e-5
    assert 0 <= pi_result < 1
    
    # E
    e_result = truncate_number(2.71828)
    assert abs(e_result - 0.71828) < 1e-5
    assert 0 <= e_result < 1


def test_truncate_number_boundary_cases():
    """Test specification 2 & 4: Boundary values at 0 and near 1"""
    # Zero decimal
    assert truncate_number(7.0) == 0.0
    
    # Very small but non-zero
    result_small = truncate_number(5.00001)
    assert 0 <= result_small < 1
    assert result_small > 0
    
    # Very close to 1
    result_large = truncate_number(5.99999)
    assert 0 <= result_large < 1
    assert result_large < 1