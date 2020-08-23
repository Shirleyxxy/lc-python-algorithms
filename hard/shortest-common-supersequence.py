## Bottom-up DP: convert to LCS problem
## Time Complexity: O(N1 * N2)
## Space Complexity: O(N1 * N2)

class Solution:
    def longestCommonSubsequence(self, str1, str2):
        n1, n2 = len(str1), len(str2)
        dp = [['' for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], key = len)

        return dp[-1][-1]


    def shortestCommonSupersequence(self, str1, str2):
        '''
        :type str1: str
        :type str2: str
        :rtype: str
        '''
        res, i, j = '', 0, 0
        for c in self.longestCommonSubsequence(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1

            while str2[j] != c:
                res += str2[j]
                j += 1

            res += c
            i, j = i + 1, j + 1

        return res + str1[i:] + str2[j:]
