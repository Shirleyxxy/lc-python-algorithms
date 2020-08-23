## BFS
## Time Complexity: O(M * N)
## Space Complexity: O(M * N)

class Solution:
    def wallsAndGates(self, rooms):
        '''
        :type rooms: List[List[int]]
        :rtype: None
        Do not return anything, modify rooms in-place instead.
        '''
        if not rooms: return
        nrow, ncol = len(rooms), len(rooms[0])
        queue = collections.deque()
        for i in range(nrow):
            for j in range(ncol):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            # keep track of the current level 
            for _ in range(len(queue)):
                i, j = queue.popleft()
                dist = rooms[i][j] + 1
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for d in directions:
                    new_i, new_j = i + d[0], j + d[1]
                    if 0 <= new_i < nrow and 0 <= new_j < ncol and rooms[new_i][new_j] == 2147483647:
                        rooms[new_i][new_j] = dist
                        queue.append((new_i, new_j))
