from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Handle edge cases
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    min_distance = float('inf')
    closest_pair = None
    
    # Compare all pairs of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            
            if distance < min_distance:
                min_distance = distance
                # Return in order (smaller, larger)
                if numbers[i] <= numbers[j]:
                    closest_pair = (numbers[i], numbers[j])
                else:
                    closest_pair = (numbers[j], numbers[i])
    
    return closest_pair


# Test the function with the provided examples
if __name__ == "__main__":
    # Test case 1
    result1 = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    print(f"Test 1: {result1}")  # Expected: (2.0, 2.2)
    
    # Test case 2
    result2 = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    print(f"Test 2: {result2}")  # Expected: (2.0, 2.0)
    
    # Additional test cases
    result3 = find_closest_elements([10.0, 5.0, 3.0, 8.0])
    print(f"Test 3: {result3}")  # Expected: (5.0, 3.0) -> (3.0, 5.0)
    
    result4 = find_closest_elements([1.5, 1.6])
    print(f"Test 4: {result4}")  # Expected: (1.5, 1.6)