## Intuition
## We need at least n - 1 cables to connect all the nodes
## So if len(connections) < n - 1, we can directly return -1.

## If we have enough cables (at least n-1 connections),
## we only need to count the number of connected networks (connected components).
## To connect two unconnected networks, we need 1 cable.
## The number of operations we need = number of connected components - 1

## We use DFS to count the number of connected components.

## Time complexity: O(connections)
## Space complexity: O(N)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1

        # construct the graph
        graph = defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        visited = [False] * n

        # count number of connected components using DFS
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in graph[i]:
                dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count - 1
