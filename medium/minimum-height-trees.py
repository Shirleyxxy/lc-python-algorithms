## Strategy: leaves can't give us MHT, we can remove them from the graph and remove their edges too.
## Prune the leaves until we are left with one or two nodes which will be the roots for MHTs.

## Time Complexity: O(V + E)
## Space Complexity: O(V + E)

from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        '''
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        '''
        if n <= 0: return []
        if n == 1: return [0]

        in_degrees = {i:0 for i in range(n)}
        graph = {i:[] for i in range(n)}

        for edge in edges:
            n1, n2 = edge[0], edge[1]
            # undirected graph
            graph[n1].append(n2)
            graph[n2].append(n1)
            in_degrees[n1] += 1
            in_degrees[n2] += 1

        leaves = deque([node for node in in_degrees if in_degrees[node] == 1])

        total_nodes = n
        # keep removing leaves and related edges until we reach one or two nodes  
        while total_nodes > 2:
            num_leaves = len(leaves)
            total_nodes -= num_leaves
            for i in range(num_leaves):
                leaf = leaves.popleft()
                for child in graph[leaf]:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 1:
                        leaves.append(child)
        return list(leaves)
