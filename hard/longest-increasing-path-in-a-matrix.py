## DFS + Memoization
## Time Complexity: O(nrows * ncols)
## Space Complexity: O(nrows * ncols)

class Solution:
    def longestIncreasingPath(self, matrix):
        '''
        :type matrix: List[List[int]]
        :rtype: int
        '''
        if not matrix or not matrix[0]:
            return 0
        nrows, ncols = len(matrix), len(matrix[0])
        dp = [[0] * ncols for _ in range(nrows)]
        max_len = 0

        def dfs(i, j):
            '''
            Top-down recursive function.
            '''
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                     dfs(i-1, j) if i > 0 and val > matrix[i-1][j] else 0,
                     dfs(i, j-1) if j > 0 and val > matrix[i][j-1] else 0,
                     dfs(i+1, j) if i < nrows-1 and val > matrix[i+1][j] else 0,
                     dfs(i, j+1) if j < ncols-1 and val > matrix[i][j+1] else 0
                )
            return dp[i][j]

        for i in range(nrows):
            for j in range(ncols):
                max_len = max(max_len, dfs(i, j))
        return max_len
