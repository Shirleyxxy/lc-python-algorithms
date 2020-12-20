## DFS
## Similar to number of islands

## Time Complexity: O(N^2) - the complete matrix of size N^2 is traversed
## Space Complexity: O(N) 
class Solution:
    def findCircleNum(self, M):
        '''
        :type M: List[List[int]]
        :rtype: int
        '''
        if not M: return 0
        num_circles = 0
        seen = set()

        def dfs(node):
            for i, val in enumerate(M[node]):
                if val == 1 and i not in seen:
                    seen.add(i)
                    dfs(i)

        ## DFS starting from every node
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                num_circles += 1
        return num_circles
