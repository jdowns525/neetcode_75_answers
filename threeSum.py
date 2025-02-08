def threeSum(nums):
    nums.sort()  # Sort the array to use two pointers and manage duplicates
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate elements for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum
    return result

#Explanation:

#Sorting helps manage duplicates and enables the two-pointer approach.
#Time Complexity: O(n²)
#Space Complexity: O(1) extra space (ignoring the space for the output)
