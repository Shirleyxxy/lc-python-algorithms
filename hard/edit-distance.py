## Bottom-up DP
## Time Complexity: O(N1 * N2)
## Space Complexity: O(N1 * N2)

class Solution:
    def minDistance(self, word1, word2):
        '''
        :type word1: str
        :type word2: str
        :rtype: int
        '''
        n1, n2 = len(word1), len(word2)
        dp = [[float('inf') for _ in range(n2+1)] for _ in range(n1+1)]

        # Base case: if word2 is empty, we can delete all the characters of word1 to match word2
        for i in range(n1+1):
            dp[i][0] = i
        # Base case: if word1 is empty, we can delete all the characters of word2 to match word1
        for j in range(n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # not match: 1 more operation needed + min(replace, delete, insert)
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[n1][n2]
