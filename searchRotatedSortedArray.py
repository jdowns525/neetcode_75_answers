def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # Check if mid is the target
        if nums[mid] == target:
            return mid
        
        # Determine if the left half is sorted
        if nums[left] <= nums[mid]:
            # If target is in the range of the sorted left half, adjust right pointer.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Otherwise, the right half must be sorted.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1  # Target not found

#Explanation:

#At each step, we determine which segment is sorted and narrow our search.
#Time Complexity: O(log n)
#Space Complexity: O(1)
