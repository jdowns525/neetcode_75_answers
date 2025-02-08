from collections import Counter

def isAnagram(s, t):
    # Compare the character counts in both strings
    return Counter(s) == Counter(t)

# Example usage:
# print(isAnagram("anagram", "nagaram"))

#Explanation:

#The Counter from the collections module efficiently counts characters.
#Time Complexity: O(n)
#Space Complexity: O(n)
