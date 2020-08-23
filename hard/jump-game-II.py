## Solution 1: DP
## Time Complexity: O(N^2)
## Space Complexity: O(N)
## dp[i]: minimum jumps needed to reach index i
## Time Limit Exceeded
class Solution:
    def jump(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for start in range(len(nums)-1):
            end = start + 1
            while end <= start + nums[start] and end < len(nums):
                dp[end] = min(dp[end], dp[start]+1)
                end += 1
        return dp[len(nums)-1]


## Solution 2: BFS
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def jump(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        start, end, step = 0, 0, 0
        while end < len(nums)-1:
            start, end = end+1, max([i+nums[i] for i in range(start, end+1)])
            step += 1
        return step
