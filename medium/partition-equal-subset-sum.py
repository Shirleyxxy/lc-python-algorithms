## Bottom-up DP
## Time Complexity: O(N*S)
## Space Complexity: O(N*S)

class Solution:
    def canPartition(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        n, s = len(nums), sum(nums)
        if s % 2 == 1: return False
        dp = [[False for _ in range(s//2+1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for j in range(1, s//2+1):
            dp[0][j] = (nums[0] == j)

        for i in range(1, n):
            for j in range(1, s//2+1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]]
        return dp[n-1][s//2]


## Space Optimized Solution
## Time Complexity: O(N*S)
## Space Complexity: O(S)

class Solution:
    def canPartition(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        s = sum(nums)
        if s % 2 == 1: return False
        target_s = s // 2
        dp = [True] + [False] * target_s
        for num in nums:
            for s in range(target_s, num-1, -1):
                dp[s] = dp[s] or dp[s-num]
        return dp[target_s]
