## Similar problem: paint house
## dp[i]: the maximum amount of money you can rob from house 1 to house i

## Solution 1 - Bottom up DP
## Time Complexity: O(N)
## Space Complexity: O(N)

## Base case:
## f(0) = nums[0]
## f(1) = max(nums[0], nums[1])

## State transition:
## f(k) = max(num[k]+f(k-2), f(k-1))

class Solution:
    def rob(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]


## Solution 2 - Bottom up DP with constant space
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def rob(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(num + prev, curr)
            # temp = prev  # nums[i-2]
            # prev = curr  # nums[i-1]
            # curr = max(prev, num + temp)
        return curr
