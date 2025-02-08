def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)
    
    # Add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

# Example usage:
# print(insert([[1,3],[6,9]], [2,5]))

#Explanation:

#The algorithm carefully distinguishes between intervals that are completely before, overlapping, and completely after the new interval.
#Time Complexity: O(n)
#Space Complexity: O(n)
