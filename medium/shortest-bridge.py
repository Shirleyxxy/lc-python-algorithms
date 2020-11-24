## DFS + BFS
## Time Complexity: O(N)
## Space Complexity: O(N)

import collections

class Solution:
    def shortestBridge(self, A):
        '''
        :type A: List[List[int]]
        :rtype: int
        '''
        found = False
        # for BFS
        queue = collections.deque()

        def dfs(i, j):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
                return
            A[i][j] = '#'
            # for BFS
            queue.append((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        ## find the first island
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    # use DFS to find all connected '1' locations for the first island
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        # BFS to expand the first island
        steps = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            # level by level
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for d in directions:
                    new_i, new_j = i + d[0], j + d[1]
                    if new_i < 0 or new_i >= len(A) or new_j < 0 or new_j >= len(A[0]) or A[new_i][new_j] == '#':
                        continue
                    if A[new_i][new_j] == 0:
                        A[new_i][new_j] = '*'
                        queue.append((new_i, new_j))
                    # as soon as we find another island
                    # return the number of steps (a.k.a number of levels traversed)
                    if A[new_i][new_j] == 1:
                        return steps
            steps += 1
