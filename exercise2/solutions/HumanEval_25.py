from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Handle edge cases
    if n <= 1:
        return []
    
    factors = []
    
    # Check for factor 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 2
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


# Test the function with the provided examples
if __name__ == "__main__":
    print(factorize(8))   # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
    
    # Additional test cases
    print(factorize(1))   # []
    print(factorize(2))   # [2]
    print(factorize(13))  # [13]
    print(factorize(12))  # [2, 2, 3]