## Time Complexity: O(logN) for insertion, O(1) for finding the median
## Space Complexity: O(N)

from heapq import *

class MedianFinder:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def addNum(self, num):
        '''
        :type num: int
        '''
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # rebalance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        '''
        :rtype: float
        '''
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0] / 1.0
