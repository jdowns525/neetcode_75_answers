def letterCombinations(digits):
    if not digits:
        return []
    
    # Mapping of digit to corresponding letters (as on a phone keypad)
    phone = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }
    
    result = []
    
    def backtrack(index, path):
        # If the current combination has reached the length of digits, add to result
        if index == len(digits):
            result.append("".join(path))
            return
        # Iterate through the letters that the current digit can represent
        possible_letters = phone[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()  # Backtrack: remove the last letter added

    backtrack(0, [])
    return result

# Example usage:
# print(letterCombinations("23"))

#Explanation:

#The recursive function backtrack constructs combinations letter by letter.
#When the length of the current path equals the number of digits, a complete combination is formed.
#Time Complexity: O(4^n) in the worst-case (each digit mapping to 4 letters)
#Space Complexity: O(n) for recursion stack and temporary combination storage
