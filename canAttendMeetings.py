def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        # If the current meeting starts before the previous meeting ends, return False
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

# Example usage:
# print(canAttendMeetings([[0,30],[5,10],[15,20]]))

#Explanation:

#Overlapping intervals will have the start time of one meeting less than the end time of the previous.
#Time Complexity: O(n log n)
#Space Complexity: O(1)
