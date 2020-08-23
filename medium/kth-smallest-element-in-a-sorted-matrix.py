## Time Complexity: O(KlogN)
## Space Complexity: O(N)

from heapq import *

class Solution:
    def kthSmallest(self, matrix, k):
        '''
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        '''
        min_heap = []
        for i in range(min(k, len(matrix))):
            heappush(min_heap, (matrix[i][0], i, 0))

        num_count = 0
        while min_heap:
            num, i, j = heappop(min_heap)
            num_count += 1
            if num_count == k: return num
            if j+1 < len(matrix[i]):
                heappush(min_heap, (matrix[i][j+1], i, j+1))
