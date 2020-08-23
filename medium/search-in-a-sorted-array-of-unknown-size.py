## Time Complexity: O(logN)
## Space Complexity: O(1)

# '''
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation.
# '''
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        '''
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        '''
        # find the search boundaries
        start, end = 0, 1
        while reader.get(end) < target:
            new_start = start + 1
            end += (end - start + 1) * 2
            start = new_start
        # binary search
        while start <= end:
            mid = start + (end - start) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
