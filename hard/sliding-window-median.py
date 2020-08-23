## Time Complexity: O(N * K)
## Space Complexity: O(K)

class Solution:
    def __init__(self):
        self.max_heap, self.min_heap = [], []
        self.medians = []


    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


    def insert(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)


    def remove(self, heap, num):
        idx = heap.index(num)
        heap[idx] = heap[-1]
        del heap[-1]
        heapify(heap)


    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0] / 1.0


    def medianSlidingWindow(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        '''
        for i in range(len(nums)):
            self.insert(nums[i])
            self.rebalance_heaps()
            if i - k + 1 >= 0:
                self.medians.append(self.find_median())
                num_to_be_removed = nums[i-k+1]
                if num_to_be_removed <= -self.max_heap[0]:
                    self.remove(self.max_heap, -num_to_be_removed)
                else:
                    self.remove(self.min_heap, num_to_be_removed)
                self.rebalance_heaps()
        return self.medians
