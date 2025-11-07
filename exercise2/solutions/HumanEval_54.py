def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return set(s0) == set(s1)


# Test the function with the provided examples
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # Additional test cases for edge cases
    print(same_chars('', ''))  # True - both empty
    print(same_chars('a', ''))  # False - one empty
    print(same_chars('', 'a'))  # False - one empty
    print(same_chars('a', 'a'))  # True - single character
    print(same_chars('a', 'b'))  # False - different single characters
    print(same_chars('aaa', 'a'))  # True - same character repeated