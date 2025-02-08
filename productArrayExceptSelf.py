def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n  # Initialize the output array with 1s

    # Left pass: product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Right pass: product of all elements to the right of each index
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

#Explanation:

#The first loop fills output[i] with the product of all elements to the left of i.
#The second loop multiplies each output[i] by the product of all elements to the right.
#Time Complexity: O(n)
#Space Complexity: O(1) extra space (ignoring the output array)
