## Similar to number of islands & max area of island
## DFS, backtracking, set

## The key to the solution is to find a way to represent a distinct shape.
## We can describe the shape by describing its moving directions (u, d, l, r).
## Note that we need to count backtracking as a moving direction (b) as well.

## Example:
## [1, 1, 0]
## [1, 0, 0]
## [0, 0, 0]
## [1, 1, 0]
## [0, 1, 0]

## [[1,1,0],[1,0,0],[0,0,0],[1,1,0],[0,1,0]]

## two distinct shapes: "sdbrbb", "srdbbb"

## Time complexity: O(M * N)
## Space complexity: O(M * N)

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        islands = set()

        def dfs(i, j, path):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] != 1:
                return ""
            grid[i][j] = "#" # mark as visited
            return path + dfs(i-1, j, "u") + dfs(i+1, j, "d") + dfs(i, j-1, "l") + dfs(i, j+1, "r") + "b"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands.add(dfs(i, j, "s"))

        #print(islands)
        return len(islands)
