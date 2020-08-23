## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def findPeakElement(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[mid+1]:
                start = mid + 1
            else:
                end = mid
        # at the end of the while loop, start == end
        return start
