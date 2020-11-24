## N = # of input equations
## M = # of queries 
## Time Complexity: O(M * N)
## Space Complexity: O(N)

import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        '''
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        '''

        def build_graph(equations, values):
            G = collections.defaultdict(list)
            for eq, val in zip(equations, values):
                source, dest = eq[0], eq[1]
                G[source].append((dest, val))
                G[dest].append((source, 1.0 / val))
            return G

        def evaluate_dfs(s, e, seen, G, value):
            if s not in G or e not in G or s in seen:
                return -1.0
            if s == e:
                return value
            seen.add(s)
            for node in G[s]:
                prod = evaluate_dfs(node[0], e, seen, G, node[1] * value)
                if prod != -1.0:
                    return prod
            return -1.0

        G = build_graph(equations, values)
        return [evaluate_dfs(s, e, set(), G, 1.0) for s, e in queries]
