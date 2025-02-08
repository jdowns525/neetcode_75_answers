def generateParenthesis(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        # When the current string is of the correct length, add to result
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # If we can add an opening parenthesis, do so
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        # Add a closing parenthesis only if it won't exceed the number of opening ones
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

# Example usage:
# print(generateParenthesis(3))

#Explanation:

#The recursive function backtrack builds valid strings while ensuring constraints.
#Time Complexity: Catalan number complexity, roughly O(4^n / (n^(3/2)))
#Space Complexity: O(n) for recursion stack
