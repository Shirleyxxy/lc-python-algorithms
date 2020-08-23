## 1. sum(s1) - sum(s2) = S (target)
## sum(nums) = total sum of all the numbers
## 2. sum(s1) + sum(s2) = sum(nums)
## add the equations 1 & 2: 2 * sum(s1) = S + sum(nums)
## sum(s1) = (S + sum(nums)) // 2
## Convert the problem to "find the count of subsets of the given numbers
## whose sum is equal to (S + sum(nums)) // 2"

## Bottom-up DP
## Time Complexity: O(N*S)
## Space Complexity: O(S)

class Solution:
    def findTargetSumWays(self, nums, S):
        '''
        :type nums: List[int]
        :type S: int
        :rtype: int
        '''
        total_sum = sum(nums)
        if total_sum < abs(S) or (total_sum + S) % 2 == 1:
            return 0
        target_s = (total_sum + S) // 2
        dp = [1] + [0] * target_s
        for num in nums:
            for s in range(target_s, num-1, -1):
                dp[s] += dp[s-num]
        return dp[target_s]
