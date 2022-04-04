## Time complexity: O(N)
## Space complexity: O(1)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates[2:]:
            if (x - x0) * (y1 - y0) != (x1 - x0) * (y - y0):
                return False
        return True
