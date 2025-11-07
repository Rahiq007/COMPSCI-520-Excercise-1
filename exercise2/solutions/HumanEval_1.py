from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Handle empty input
    if not paren_string:
        return []
    
    result = []
    current_group = ""
    open_count = 0
    
    for char in paren_string:
        if char == '(':
            current_group += char
            open_count += 1
        elif char == ')':
            current_group += char
            open_count -= 1
            
            # When open_count reaches 0, we have a complete balanced group
            if open_count == 0:
                result.append(current_group)
                current_group = ""
    
    return result