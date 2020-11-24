## Brute force
class Solution:
    def pivotIndex(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return -1
        if len(nums) == 1: return 0
        for i, num in enumerate(nums):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1


## How to optimize it?
## Prefix sum
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def pivotIndex(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return -1
        S, left_sum = sum(nums), 0
        for i, num in enumerate(nums):
            if left_sum == S - left_sum - nums[i]:
                return i
            else:
                left_sum += nums[i]
        return -1
