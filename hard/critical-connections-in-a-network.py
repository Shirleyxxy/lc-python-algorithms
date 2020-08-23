## An edge is a critical connection if and only if it is not in a cycle.
## So we find all the edges in the cycles, discard them;
## Then the remaining connections are a complete collection of critical connections

## Time Complexity: O(|E|)
## Space Complexity: O(|E|)
class Solution:
    def criticalConnections(self, n, connections):
        '''
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        '''
        # create the graph
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])

        # the smaller node is placed before the larger node
        connections = set(map(tuple, (map(sorted, connections))))
        # rank: the depth of a node during DFS; starting node has rank 0
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                # skip the parent node
                # why we initialize the rank to -2 rather than -1 (for the case when depth == 0)
                if rank[neighbor] == depth-1:
                    continue
                back_depth = dfs(neighbor, depth+1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            # the first time calling dfs(node) will return the minimum rank it finds
            return min_back_depth
        # we don't need to loop over all nodes since it is a connected graph
        dfs(0, 0)
        return list(connections)
