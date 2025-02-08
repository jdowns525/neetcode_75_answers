def twoSum(nums, target):
    # Dictionary to map number -> its index
    num_to_index = {}
    # Iterate over the list with index and value
    for i, num in enumerate(nums):
        complement = target - num
        # If the complement is found, return the pair of indices
        if complement in num_to_index:
            return [num_to_index[complement], i]
        # Store the index of the current number for future reference
        num_to_index[num] = i
    # If no solution is found (should not happen as per problem statement)
    return []

#Explanation:

#We loop over nums once, checking for the existence of target - num in our dictionary.
#If found, we return the stored index and the current index.
#Otherwise, we add the current number with its index to the dictionary.
#Time Complexity: O(n)
#Space Complexity: O(n
