## BFS
## number of minutes elapsed = number of levels
## Time Complexity: O(N), N is the size of the grid
## Space Complexity: O(N), N is the size of the grid

from collections import deque
class Solution:
    def orangesRotting(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        nrow, ncol = len(grid), len(grid[0])
        fresh_cnt = 0
        queue = deque()
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1: fresh_cnt += 1
                if grid[i][j] == 2: queue.append((i, j))
        time = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for d in directions:
                    new_i, new_j = i + d[0], j + d[1]
                    if 0 <= new_i < nrow and 0 <= new_j < ncol and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh_cnt -= 1
                        queue.append((new_i, new_j))
            time += 1
        return max(time-1, 0) if fresh_cnt == 0 else -1
