## DFS (Recursion) + Backtracking
## Path exploration in a graph data structure
## Time Complexity: O(2^N * N)
## Space Complexity: O(2^N * N) + O(N) for the recursion stack --> O(2^N * N)

## There could be at most Sum(i from 0 to N-2) 2^i = 2^(N-1)-1 possible paths
## between the starting and ending nodes
## For each path, there could be at most N-2 intermediate nodes
## i.e. It takes O(N) time to build a path
## Loose upper-bound for time complexity: O(2^N * N)

class Solution:
    def allPathsSourceTarget(self, graph):
        '''
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        '''
        all_paths = []
        # start from the source to kick off the backtracking exploration
        self.dfs(graph, 0, [0], all_paths)
        return all_paths

    def dfs(self, graph, curr_node, curr_path, all_paths):
        # stop the exploration (terminate the recursion) when we encounter the target node
        if curr_node == len(graph) - 1:
            # note: list(curr_path) works; using curr_path won't work
            # Functional arguments in Python are passed by reference
            # curr_path is a list; we should append a **copy** of the list
            # to the result in the terminal condition; otherwise, curr_path
            # will be affected by the recursive processing
            # the list constructor list(curr_path) will make a shallow copy
            # slicing also works: curr_path[:]
            all_paths.append(curr_path[:])

        # enumerate through all the neighbor nodes of the current node
        for node in graph[curr_node]:
            # mark the choice by appending
            curr_path.append(node)
            # recursively explore deeper
            self.dfs(graph, node, curr_path, all_paths)
            # reverse the choice (backtrack) by popping
            # before starting another exploration for the next neighbor node
            curr_path.pop()


## Nested solution
class Solution:
    def allPathsSourceTarget(self, graph):
        '''
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        '''
        all_paths = []

        def dfs(curr_node, curr_path):
            if curr_node == len(graph) - 1:
                all_paths.append(curr_path[:])
                return
            for node in graph[curr_node]:
                curr_path.append(node)
                dfs(node, curr_path)
                curr_path.pop()

        dfs(0, [0])
        return all_paths
