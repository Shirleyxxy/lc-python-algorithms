## Recursion with memoization
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
        memo = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]
        return self.search(text1, text2, 0, 0, memo)

    def search(self, s1, s2, i, j, memo):
        if memo[i][j] == -1:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] =  1 + self.search(s1, s2, i+1, j+1, memo)
            else:
                memo[i][j] = max(self.search(s1, s2, i+1, j, memo), self.search(s1, s2, i, j+1, memo))
        return memo[i][j]


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

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n1][n2]
