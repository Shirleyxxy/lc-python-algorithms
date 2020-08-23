## DFS
## Time Complexity: O(M * N)
## Space Complexity: worst case - O(M * N)
class Solution:
    def numIslands(self, grid):
        '''
        :type grid: List[List[str]]
        :rtype: int
        '''
        if not grid: return 0
        nrow, ncol = len(grid), len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]

        def dfs(i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


## DFS (Input modification)
## Iterate through each cell and if it is a land, do dfs to mark all the adjacent lands,
## then increase the counter by 1.
## Time Complexity: O(M * N)
## Space Complexity: worst case - O(M * N)
class Solution:
    def numIslands(self, grid):
        '''
        :type grid: List[List[str]]
        :rtype: int
        '''
        if not grid: return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count


    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        # mark as visited
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


## BFS
from collections import deque

class Solution:
    def numIslands(self, grid):
        '''
        :type grid: List[List[str]]
        :rtype: int
        '''
        if not grid: return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count


    def is_valid(self, grid, i, j):
        nrow, ncol = len(grid), len(grid[0])
        if i < 0 or i >= nrow or j < 0 or j >= ncol:
            return False
        return True


    def bfs(self, grid, i, j):
        queue = deque()
        queue.append((i, j))
        # mark as visited
        grid[i][j] = '#'
        while queue:
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            i, j = queue.popleft()
            for d in directions:
                new_i, new_j = i + d[0], j + d[1]
                if self.is_valid(grid, new_i, new_j) and grid[new_i][new_j] == '1':
                    queue.append((new_i, new_j))
                    grid[new_i][new_j] = '#'
