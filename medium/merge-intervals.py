## Time Complexity: O(N * logN), dominated by sorting
## Space Complexity: O(N)

class Solution:
    def merge(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        '''
        if len(intervals) < 2: return intervals
        # sort the intervals on the start time
        intervals.sort(key = lambda x: x[0])
        merged = []
        for interval in intervals:
            # if merged is empty or the current interval does not overlap
            # with the previous interval
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            # overlapping intervals; update the end
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
