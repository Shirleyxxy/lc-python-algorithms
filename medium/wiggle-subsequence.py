## Bottom-up DP
## Time Complexity: O(N^2)
## Space Complexity: O(N)

class Solution:
    def wiggleMaxLength(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return 0
        # dp[i][0]: stores the LAS ending at i such that the last two elements are in ascending order
        # dp[i][1]: stores the LAS ending at i such that the last two elements are in descending order
        # every single element can be considered as LAS of length 1
        dp = [[1 for _ in range(2)] for _ in range(len(nums))]
        max_len = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], 1 + dp[j][1])
                    max_len = max(max_len, dp[i][0])
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], 1 + dp[j][0])
                    max_len = max(max_len, dp[i][1])
        return max_len


## Linear DP
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def wiggleMaxLength(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if len(nums) < 2: return len(nums)
        up = [1 for _ in range(len(nums))]
        down = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]

        return max(up[len(nums)-1], down[len(nums)-1])


## Space-Optimized Linear DP
## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def wiggleMaxLength(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if len(nums) < 2: return len(nums)
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)
