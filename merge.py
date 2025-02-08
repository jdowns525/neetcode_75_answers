def merge(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        prev = merged[-1]
        # If the current interval overlaps with the previous, merge them
        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)
    return merged

# Example usage:
# print(merge([[1,3],[2,6],[8,10],[15,18]]))

#Explanation:

#Sorting ensures that overlapping intervals are consecutive.
#Time Complexity: O(n log n) due to sorting
#Space Complexity: O(n) for the output list
