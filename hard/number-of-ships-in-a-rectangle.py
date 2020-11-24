# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation.
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

## Time Complexity: O(10logMN)
## T(M, N, K): time for counting ships in a plane of size M * N where maximum number of ships is K.
## In worst case, all the ships are spread out in different partitions.
## T(M, N, 10) = 10T(M/2, N/2, 1) + 6C_1
## T(M, N, 1) = T(M/2, N/2, 1) + 3C_2  -- similar to binary search, T(M, N, 1) = O(logMN)
## T(M, N, K) = O(KlogMN)


class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        '''
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: int
        '''
        def divide_conquer(tr, bl):
            if tr.x < bl.x or tr.y < bl.y:
                return 0
            if tr.x == bl.x and tr.y == bl.y:
                return int(sea.hasShips(tr, bl))
            if not sea.hasShips(tr, bl):
                return 0
            x0, y0 = bl.x, bl.y
            x1, y1 = tr.x, tr.y
            x_m, y_m = (x0 + x1) // 2, (y0 + y1) // 2
            return divide_conquer(Point(x_m, y_m), bl) + \
                   divide_conquer(tr, Point(x_m+1, y_m+1)) + \
                   divide_conquer(Point(x_m, y1), Point(x0, y_m+1)) + \
                   divide_conquer(Point(x1, y_m), Point(x_m+1, y0))

        return divide_conquer(topRight, bottomLeft)
