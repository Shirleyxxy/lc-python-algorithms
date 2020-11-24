## Given a sorted array of **distinct** integers and a target value, return the index
## if the target is found. If not, return the index where it would be if it were inserted in order.

## Time Complexity: O(logN)
## Space Complexity: O(1)
class Solution:
    def searchInsert(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        if not nums: return 0
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start
