## Bottom-up DP
## Time Complexity: O(N1 * N2)
## Space Complexity: O(N1 * N2)

class Solution:
    def isInterleave(self, s1, s2, s3):
        '''
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        '''
        n1, n2, n3 = len(s1), len(s2), len(s3)
        dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]

        if n1 + n2 != n3: return False
        for i in range(n1+1):
            for j in range(n2+1):
                # if s1 and s2 are empty, then s3 must have been empty too
                if i == j == 0:
                    dp[i][j] = True
                # if s1 is empty, we check the interleaving with s2 only
                elif i == 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
                # if s2 is empty, we check the interleaving with s1 only
                elif j == 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    # if the letter of s1 and s3 match, we take whatever is matched until i-1
                    if i > 0 and s1[i-1] == s3[i+j-1]:
                        dp[i][j] = dp[i-1][j]
                    # if the letter of s2 and s3 match, we take whatever is matched until j-1
                    # |= for common letters in both s1 and s2 (equivalent to OR)
                    if j > 0 and s2[j-1] == s3[i+j-1]:
                        dp[i][j] |= dp[i][j-1]

        return dp[n1][n2]
