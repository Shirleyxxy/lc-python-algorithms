## Time Complexity: O(nrows * ncols)
## Space Complexity: O(1)

class Solution:
    def islandPerimeter(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        nrows, ncols = len(grid), len(grid[0])
        perimeter = 0

        def checkEdges(i, j):
            up = 1 if i > 0 and grid[i-1][j] == 1 else 0
            down = 1 if i < nrows-1 and grid[i+1][j] == 1 else 0
            left = 1 if j > 0 and grid[i][j-1] == 1 else 0
            right = 1 if j < ncols-1 and grid[i][j+1] == 1 else 0
            return 4 - (up + down + left + right)

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    perimeter += checkEdges(i, j)

        return perimeter
