## Use a min heap to find the Kth largest number
## Time Complexity: O(logK) for the add function
## Space Complexity: O(K) for storing numbers in the heap

from heapq import *

class KthLargest:

    def __init__(self, k, nums):
        '''
        :type k: int
        :type nums: List[int]
        '''
        self.k = k
        self.nums = nums
        heapify(self.nums)
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val):
        '''
        :type val: int
        '''
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)
        return self.nums[0]
