## Time Complexity: O(NlogM)
## Space Complexity: O(M)

from heapq import *

class Solution:
    def smallestRange(self, nums):
        '''
        :type nums: List[List[int]]
        :rtype: List[int]
        '''
        min_heap = []
        for i, lst in enumerate(nums):
            heappush(min_heap, (lst[0], i, 0))

        res = float('-inf'), float('inf')
        right = max(lst[0] for lst in nums)
        while min_heap:
            left, i, j = heappop(min_heap)
            if right - left < res[1] - res[0]:
                res = left, right
            if j + 1 == len(nums[i]): return res
            val = nums[i][j+1]
            right = max(right, val)
            heappush(min_heap, (val, i, j+1))
