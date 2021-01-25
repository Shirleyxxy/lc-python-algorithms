## Greedy
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        curr_max = global_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            global_max = max(global_max, curr_max)
        return global_max


## Dynamic Programming
## This solution is more intuition to me.
## Time Complexity: O(N)
## Space Complexity: O(1)
## Move along the array and modify the array to track
## the current local maximum sum at this given point.
class Solution:
    def maxSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum
