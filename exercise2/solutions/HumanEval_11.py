def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Handle edge case of empty strings
    if not a and not b:
        return ""
    if not a:
        return b
    if not b:
        return a
    
    # Ensure both strings have the same length by padding with leading zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Perform XOR operation character by character
    result = ""
    for i in range(max_len):
        # XOR: 0^0=0, 0^1=1, 1^0=1, 1^1=0
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    
    return result


# Test the function
if __name__ == "__main__":
    # Test case from docstring
    print(string_xor('010', '110'))  # Expected: '100'
    
    # Additional test cases
    print(string_xor('1', '1'))      # Expected: '0'
    print(string_xor('1', '0'))      # Expected: '1'
    print(string_xor('0', '0'))      # Expected: '0'
    print(string_xor('', ''))        # Expected: ''
    print(string_xor('101', '11'))   # Expected: '010' (11 becomes 011)
    print(string_xor('1010', '1100')) # Expected: '0110'