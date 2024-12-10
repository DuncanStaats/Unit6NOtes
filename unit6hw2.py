def isInteger(_users_string_):
    # Strip leading and trailing whitespace
    _users_string_ = _users_string_.strip()
    
    # Check if the string is empty after stripping
    if len(_users_string_) == 0:
        return False
    
    # Check for optional leading '+' or '-' and ensure the rest are digits
    if _users_string_[0] in ['+', '-', '&']:
        if len(_users_string_) == 1:  # Only one character which is +, - or &
            return False
        return all(char.isdigit() for char in _users_string_[1:])
    
    # Check if the string is all digits
    return all(char.isdigit() for char in _users_string_)

print(isInteger("123"))        
print(isInteger("   -456  "))  
print(isInteger("+789"))       
print(isInteger("abc"))        
print(isInteger("  "))         
print(isInteger("-"))          
