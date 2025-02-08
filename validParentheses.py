def isValid(s):
    # Mapping of closing to opening brackets for easy lookup
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in mapping.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in mapping:
            # If stack is empty or the top doesn't match the corresponding opening bracket, return False
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()  # Pop the matching opening bracket
        else:
            # In case of unexpected characters, you could choose to handle it differently.
            return False
    # If the stack is empty, all brackets matched; otherwise, not valid.
    return len(stack) == 0

# Example usage:
# print(isValid("()[]{}"))

#Explanation:

#The stack ensures that the last opened bracket is closed first.
#Time Complexity: O(n)
#Space Complexity: O(n)
