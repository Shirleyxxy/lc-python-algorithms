## Ref: https://en.wikipedia.org/wiki/Maximum_subarray_problem

## dynamic programming
## time complexity: O(N)
## space complexity: O(1)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = global_max = nums[0]
        for num in nums[1:]:
            max_ending_here = max(max_ending_here + num, num)
            global_max = max(global_max, max_ending_here)
        return global_max
