## Bottom-up DP
## Time Complexity: O(N^2)
## Space Complexity: O(N)

class Solution:
    def lengthOfLIS(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return 0
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                # if the number at the current index is bigger than the number at the previous index
                # we increment the count for LIS up to the current index
                # but if there is a bigger LIS without including the number at the current index, we
                # take that number
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
