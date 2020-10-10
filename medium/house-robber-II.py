## Time Complexity: O(N)
## Space Complexity: O(1)
## Ref: lc198 - House Robber (Space optimized version)
## Idea: The first house and the last house cannot be both robbed.
class Solution:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def no_cycle_rob(nums):
            prev, curr = 0, 0
            for num in nums:
                temp = prev
                prev = curr
                curr = max(temp + num, prev)
            return curr

        return max(no_cycle_rob(nums[:-1]), no_cycle_rob(nums[1:]))
