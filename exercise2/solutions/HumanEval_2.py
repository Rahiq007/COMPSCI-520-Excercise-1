def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Handle edge case where number might be negative
    if number < 0:
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