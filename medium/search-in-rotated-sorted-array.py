## No duplicates in the array
## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def search(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target: return mid
            # left side is sorted in ascending order
            if nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # right side is sorted in ascending order
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
