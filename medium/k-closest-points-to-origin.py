## Time Complexity: O(NlogK)
## Space Complexity: O(K)

class Solution:
    def distance(self, point):
        # ignoring sqrt to calculate the distance
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points, K):
        '''
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        '''
        max_heap = []
        for point in points:
            heappush(max_heap, (-self.distance(point), point))
            if len(max_heap) > K:
                heappop(max_heap)

        res = []
        while max_heap:
            res.append(heappop(max_heap)[1])
        return res
