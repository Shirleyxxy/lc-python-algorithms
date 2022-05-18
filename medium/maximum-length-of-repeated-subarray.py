## Same idea to longest common substring
## Bottom-up DP

## dp[i][j] = length of longest common substring for A[:i] and B[:j]
## dp[i][j] = 1 + dp[i-1][j-1] if A[i-1] == B[j-1]

## time complexity: O(n1 * n2)
## space complexity: O(n1 * n2)


class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n1, n2 = len(A), len(B)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        max_len = 0

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    max_len = max(max_len, dp[i][j])

        return max_len
