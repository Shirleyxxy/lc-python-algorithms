## Time Complexity: O(N * logN), dominated by sorting and N extract-min operations on heap (each takes O(logN)).
## Space Complexity: O(N)

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: int
        '''
        # Sort the meeting intervals by the starting time
        intervals.sort(key = lambda x: x[0])
        # Store the end time of meetings
        # Keep track of how many rooms are needed
        min_heap = []
        for interval in intervals:
            # check if the min of the heap (a.k.a the room that holds the meeting
            # with the earliest end time) is available or not
            if not min_heap or min_heap[0] > interval[0]:
                # need to allocate a room
                heappush(min_heap, interval[1])
            # two intervals can use the same room
            else:
                # pop, then push the next meeting that
                # can use the previously allocated room
                heapreplace(min_heap, interval[1])

        return len(min_heap)
