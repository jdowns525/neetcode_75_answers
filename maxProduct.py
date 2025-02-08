def maxProduct(nums):
    if not nums:
        return 0

    # Initialize maximum, minimum products, and the result with the first element.
    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        # If the current number is negative, swap max_prod and min_prod
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        # Calculate the new maximum and minimum products
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        # Update the result with the maximum product found so far
        result = max(result, max_prod)
    return result

#Explanation:

#Swapping when a negative is encountered is crucial.
#Time Complexity: O(n)
#Space Complexity: O(1)
