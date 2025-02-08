def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        # If the current interval starts before the previous one ends, it overlaps
        if intervals[i][0] < prev_end:
            count += 1
        else:
            prev_end = intervals[i][1]
    
    return count

# Example usage:
# print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

#Explanation:

#Sorting by end time ensures that we always choose the interval that finishes earliest.
#Time Complexity: O(n log n)
#Space Complexity: O(1) (ignoring the input)
