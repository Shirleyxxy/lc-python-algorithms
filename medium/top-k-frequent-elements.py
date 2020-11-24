## Time Complexity: O(N + NlogK)
## Space Complexity: O(N)

from heapq import *


class Solution:
    def topKFrequent(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        '''
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        min_heap = []
        for num, freq in num_freq.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)

        res = []
        while min_heap:
            res.append(heappop(min_heap)[1])
        return res
