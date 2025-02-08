def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # If mid element is greater than the rightmost, the minimum must be to the right of mid
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum is at mid or to the left of mid
            right = mid
    return nums[left]

#Explanation:

#The key observation is that the unsorted portion will contain the minimum.
#Time Complexity: O(log n)
#Space Complexity: O(1)
