## DFS
## Similar to number of islands
## Time Complexity: O(nrows * ncols)
## Space Complexity: O(nrows * ncols)


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        nrows, ncols = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= nrows or j < 0 or j >= ncols or grid[i][j] != 1:
                return 0
            grid[i][j] = "#"  # mark as visited
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
