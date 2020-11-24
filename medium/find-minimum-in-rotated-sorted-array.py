## Modified Binary Search
## No duplicates in the array; all the integers are unique
## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def findMin(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        start, end = 0, len(nums)-1
        # start and end both converge to the minimum index
        # do not use <=
        while start < end:
            mid = start + (end - start) // 2
            # the pivot must be to the right of the mid
            if nums[mid] > nums[end]:
                start = mid + 1
            # nums[mid] <= nums[end]
            # the pivot must be at mid or to the left of the mid
            else:
                end = mid
        # at this point, start and end converge to a single index for min value
        return nums[start]
