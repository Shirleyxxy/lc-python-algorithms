## V: count of distinct numbers
## E: total number of the rules
## N: count of numbers in all sequences
## Time Complexity: O(V + E), upper bound is O(V + N)
## Space Complexity: O(V + N)

from collections import deque, defaultdict

class Solution:
    def sequenceReconstruction(self, org, seqs):
        '''
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        '''
        sorted_order = []
        if len(org) == 0: return False

        # Initialize the graph
        in_degrees = defaultdict(int)
        graph = defaultdict(list)
        for seq in seqs:
            for node in seq:
                in_degrees[node] = 0
                graph[node] = []

        # Build the graph
        for seq in seqs:
            for i in range(1, len(seq)):
                parent, child = seq[i-1], seq[i]
                graph[parent].append(child)
                in_degrees[child] += 1

        # If we have more / fewer ordering rules than the numbers in the original sequence,
        # we'll not able to uniquely construct the sequence
        if len(in_degrees) != len(org): return False

        sources = deque([node for node in in_degrees if in_degrees[node] == 0])

        # Ensure we do not have more than one source while finding the topological
        # ordering of numbers (the topological order is unique)
        while len(sources) == 1:
            node = sources.popleft()
            sorted_order.append(node)
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        return True if sorted_order == org else False
