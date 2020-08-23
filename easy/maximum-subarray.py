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
