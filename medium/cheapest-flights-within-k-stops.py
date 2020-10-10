## Solution 1 - BFS
## seen[node] - the min cost from source to the current city
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst: return 0
        d, seen = defaultdict(list), defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            d[u].append((v, p))

        queue = deque([(src, -1, 0)])
        while queue:
            node, stops, cost = queue.popleft()
            if node == dst or stops == K: continue
            for neighbor, price in d[node]:
                if cost + price >= seen[neighbor]:
                    continue
                else:
                    seen[neighbor] = cost + price
                    queue.append((neighbor, stops+1, cost+price))
        return seen[dst] if seen[dst] < float('inf') else -1


## Solution 2 - Dijkstra's Algorithm
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        adjList = defaultdict(list)
        for start, end, price in flights:
            adjList[start].append((end, price))

        heap = [(0, -1, src)]  # price | stops | city
        while heap:
            cur_price, stops, city = heappop(heap)
            if stops > K: continue
            # return immediately since dijkstra always finds lowest distance
            if city == dst: return cur_price
            for neighbor, neighbor_price in adjList[city]:
                heappush(heap, (cur_price+neighbor_price, stops+1, neighbor))
        return -1
