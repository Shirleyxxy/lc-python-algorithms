## Time Complexity: O(NlogK)
## Space Complexity: O(K)

from heapq import *

class Solution:
    def findKthLargest(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: int
        '''
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]
