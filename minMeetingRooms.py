import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    # Initialize a min-heap with the end time of the first meeting
    heap = [intervals[0][1]]
    
    for interval in intervals[1:]:
        # If the earliest ending meeting is finished before the current meeting starts, reuse that room
        if heap[0] <= interval[0]:
            heapq.heappop(heap)
        # Allocate the current meeting's end time into the heap (new or reused room)
        heapq.heappush(heap, interval[1])
    
    # The size of the heap represents the number of rooms required
    return len(heap)

# Example usage:
# print(minMeetingRooms([[0,30],[5,10],[15,20]]))

#Explanation:

#The min-heap always contains the end times of meetings currently using rooms.
#Time Complexity: O(n log n) due to sorting and heap operations
#Space Complexity: O(n)
