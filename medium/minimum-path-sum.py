## Recursion with memoization
## Time: O(2^(M+N))
## Space: O(M * N) for memo; O(M + N) for recursion depth
class Solution:
    def minPathSum(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        memo = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def minPathSumRec(r, c):
            if r == len(grid) or c == len(grid[0]):
                return float('inf')
            elif r == len(grid)-1 and c == len(grid[0])-1:
                return grid[r][c]
            elif memo[r][c] != float('inf'):
                return memo[r][c]
            else:
                right = minPathSumRec(r, c+1)
                down = minPathSumRec(r+1, c)
                memo[r][c] = grid[r][c] + min(right, down)
                return memo[r][c]

        return minPathSumRec(0, 0)


## Bottom-up DP
## Time: O(M * N)
## Space: O(M * N)
class Solution:
    def minPathSum(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        nrows, ncols = len(grid), len(grid[0])
        dp = [[0] * ncols for _ in range(nrows)]
        # base cases
        dp[0][0] = grid[0][0]
        for c in range(1, ncols):
            dp[0][c] = grid[0][c] + dp[0][c-1]
        for r in range(1, nrows):
            dp[r][0] = grid[r][0] + dp[r-1][0]
        for r in range(1, nrows):
            for c in range(1, ncols):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]


## DP (Modify the grid in-place)
## Time: O(M * N)
## Space: O(1)
class Solution:
    def minPathSum(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        nrows, ncols = len(grid), len(grid[0])
        for i in range(nrows):
            for j in range(ncols):
                if i == j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
