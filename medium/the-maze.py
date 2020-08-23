## BFS
## Time Complexity: O(nrows * ncols)
## Space Complexity: O(nrows * ncols)

class Solution:
    def hasPath(self, maze, start, destination):
        '''
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        '''
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        nrows, ncols = len(maze), len(maze[0])
        visited = [[False] * ncols for _ in range(nrows)]

        # queue for new start points
        queue = collections.deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            pos = queue.popleft()
            # check if the ball reaches the destination
            if pos[0] == destination[0] and pos[1] == destination[1]:
                return True
            for dir in directions:
                # roll the ball until it hits the wall
                row, col = pos[0] + dir[0], pos[1] + dir[1]
                while 0 <= row < nrows and 0 <= col < ncols and maze[row][col] == 0:
                    row += dir[0]
                    col += dir[1]
                # (row, col) locates at a wall when exiting the while loop
                # needs to go back 1 step
                (new_r, new_c) = (row - dir[0], col - dir[1])
                # check if the new starting position has been visited
                if not visited[new_r][new_c]:
                    queue.append((new_r, new_c))
                    visited[new_r][new_c] = True
        return False
