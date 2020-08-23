## Time Complexity: O(NlogN)
## Space Complexity: O(N)

class Solution:
    def findRightInterval(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: List[int]
        '''
        result = [-1] * len(intervals)
        max_start_heap, max_end_heap = [], []
        for i in range(len(intervals)):
            heappush(max_start_heap, (-intervals[i][0], i))
            heappush(max_end_heap, (-intervals[i][1], i))

        for _ in range(len(intervals)):
            top_end, i = heappop(max_end_heap)
            if max_start_heap and -max_start_heap[0][0] >= -top_end:
                curr_start, curr_start_i = heappop(max_start_heap)
                while max_start_heap and -max_start_heap[0][0] >= -top_end:
                    curr_start, curr_start_i = heappop(max_start_heap)
                result[i] = curr_start_i
                heappush(max_start_heap, (curr_start, curr_start_i))
        return result
