## Time Complexity: O(NlogN)
## Space Complexity: O(N)

from heapq import *

class Solution:
    def connectSticks(self, sticks):
        '''
        :type sticks: List[int]
        :rtype: int
        '''
        min_heap, min_cost = [], 0
        for stick in sticks:
            heappush(min_heap, stick)
        while len(min_heap) > 1:
            tmp = heappop(min_heap) + heappop(min_heap)
            min_cost += tmp
            heappush(min_heap, tmp)
        return min_cost
