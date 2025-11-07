def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    BUG INJECTED: Changed condition from < 0 to <= 0
    This is a realistic off-by-one error where the developer incorrectly includes 0 in the error case.
    Zero is a valid positive number (or at least non-negative), but this bug treats it as invalid.
    
    Expected behavior: truncate_number(0.0) should return 0.0
    Buggy behavior: truncate_number(0.0) raises ValueError
    """
    # Handle edge case where number might be negative
    if number <= 0:  # BUG: Should be < 0, not <= 0
        raise ValueError("Function expects a positive floating point number")

    # Get the integer part by converting to int (truncates towards zero)
    integer_part = int(number)

    # Return the decimal part by subtracting the integer part
    decimal_part = number - integer_part

    return decimal_part


# Test the function
if __name__ == "__main__":
    # Test cases
    print(truncate_number(3.5))    # Expected: 0.5
    print(truncate_number(1.25))   # Expected: 0.25
    print(truncate_number(2.0))    # Expected: 0.0
    print(truncate_number(0.7))    # Expected: 0.7
    print(truncate_number(10.999)) # Expected: 0.999

    # Run doctest
    import doctest
    doctest.testmod()