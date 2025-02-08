def threeSumClosest(nums, target):
    nums.sort()  # Sort the array
    n = len(nums)
    # Initialize the closest sum with an arbitrary sum of the first three elements
    closest = nums[0] + nums[1] + nums[2]
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            # Update the closest sum if the current one is nearer to target
            if abs(current_sum - target) < abs(closest - target):
                closest = current_sum
            
            # Move pointers based on how current_sum compares to target
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If current_sum equals target, it's the closest possible sum.
                return current_sum
    return closest

#Explanation:

#Sorting and the two-pointer approach reduce the time complexity significantly.
#Time Complexity: O(n²)
#Space Complexity: O(1)
