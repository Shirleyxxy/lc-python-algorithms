## Time Complexity: O(NlogN + KlogN) where N is the total number of projects and K is the number
## of projects we are selecting.
## Space Complexity: O(N)

from heapq import *

class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capitals):
        '''
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capitals: List[int]
        :rtype: int
        '''
        projects = sorted(zip(Capitals, Profits), key = lambda project: project[0])
        max_profit_heap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= W:
                heappush(max_profit_heap, -projects[i][1])
                i += 1
            if max_profit_heap:
                W += -heappop(max_profit_heap)
        return W
