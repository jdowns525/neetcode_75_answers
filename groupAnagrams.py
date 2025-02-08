from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        # Sort the string and use it as a key
        key = tuple(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())

# Example usage:
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#Explanation:

#Sorting each string yields the same key for anagrams.
#Time Complexity: O(n * k log k), where k is the maximum length of a string
#Space Complexity: O(n * k) for the dictionary storage
