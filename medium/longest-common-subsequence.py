## Bottom-up DP
## Time Complexity: O(N1 * N2)
## Space Complexity: O(N1 * N2)

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        '''
        :type text1: str
        :type text2: str
        :rtype: int
        '''
        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        max_len = 0

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                max_len = max(max_len, dp[i][j])

        return max_len
