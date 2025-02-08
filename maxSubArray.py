def maxSubArray(nums):
    # Initialize the current and global maximum with the first element
    max_current = max_global = nums[0]
    for num in nums[1:]:
        # Either start a new subarray at current element or extend the previous subarray
        max_current = max(num, max_current + num)
        # Update global maximum if needed
        max_global = max(max_global, max_current)
    return max_global

#Explanation:

#At each index, decide whether to add the current number to the existing subarray or start a new subarray.
#Time Complexity: O(n)
#Space Complexity: O(1)
