def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Handle empty string
    if not string:
        return ''
    
    # Find the longest palindromic suffix
    # Start from the full string and work towards shorter suffixes
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            # Found the longest palindromic suffix
            # The prefix is everything before this suffix
            prefix = string[:i]
            # Return original string + reverse of prefix
            return string + prefix[::-1]
    
    # This should never be reached since at minimum the last character
    # is always a palindromic suffix of length 1
    return string


# Test the implementation
if __name__ == "__main__":
    # Test cases from docstring
    print(make_palindrome(''))      # Expected: ''
    print(make_palindrome('cat'))   # Expected: 'catac'
    print(make_palindrome('cata'))  # Expected: 'catac'
    
    # Additional test cases
    print(make_palindrome('a'))     # Expected: 'a'
    print(make_palindrome('ab'))    # Expected: 'aba'
    print(make_palindrome('abc'))   # Expected: 'abcba'
    print(make_palindrome('abcd'))  # Expected: 'abcdcba'
    print(make_palindrome('racecar'))  # Expected: 'racecar' (already a palindrome)