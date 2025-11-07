from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Handle edge cases
    if len(numbers) < 2:
        return False
    
    # Check all pairs of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    
    return False


# Test the function with the provided examples
if __name__ == "__main__":
    # Test case 1
    result1 = has_close_elements([1.0, 2.0, 3.0], 0.5)
    print(f"Test 1: {result1}")  # Should be False
    
    # Test case 2
    result2 = has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    print(f"Test 2: {result2}")  # Should be True
    
    # Additional edge case tests
    print(f"Empty list: {has_close_elements([], 1.0)}")  # Should be False
    print(f"Single element: {has_close_elements([1.0], 0.5)}")  # Should be False
    print(f"Two identical elements: {has_close_elements([1.0, 1.0], 0.1)}")  # Should be True