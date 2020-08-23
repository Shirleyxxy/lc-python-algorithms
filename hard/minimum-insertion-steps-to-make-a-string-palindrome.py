## Time Complexity: O(N^2)
## Space Complexity: O(N^2)
## Bottom-up DP: convert to LPS problem

class Solution:
    def minInsertions(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        # find longest palindrome subsequence (LPS) in the string
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for start_idx in range(len(s)-1, -1, -1):
            for end_idx in range(start_idx+1, len(s)):
                if s[start_idx] == s[end_idx]:
                    dp[start_idx][end_idx] = 2 + dp[start_idx+1][end_idx-1]
                else:
                    dp[start_idx][end_idx] = max(dp[start_idx+1][end_idx], dp[start_idx][end_idx-1])

        return len(s) - dp[0][len(s)-1]
