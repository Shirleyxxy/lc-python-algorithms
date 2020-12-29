## DFS
## Similar to number of islands
## Time Complexity: O(nrows * ncols)
## Space Complexity: O(nrows * ncols)

class Solution:
    def maxAreaOfIsland(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        max_area = 0
        nrows, ncols = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < nrows and 0 <= j < ncols and grid[i][j] == 1:
                grid[i][j] = '#'
                return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i,j-1)
            return 0

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area
