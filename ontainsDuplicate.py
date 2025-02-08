def containsDuplicate(nums):
    seen = set()  # Set to store unique elements
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
    return False  # No duplicates encountered

#Explanation:

#A set provides O(1) average lookup time.
#Time Complexity: O(n)
#Space Complexity: O(n)
