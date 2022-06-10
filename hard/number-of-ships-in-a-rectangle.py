# Ref: https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/1024086/Divide-and-Conquer-or-Visual-%2B-Explanation-or-Python


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
# 	def __init__(self, x: int, y: int):
# 		self.x = x
# 		self.y = y

## time complexity: 4 * S * (log_2 max(M, N))
## maximum depth of the recursion tree: log_2 max(M, N)
## there can be at most S sub-rectangles (one per ship, so at most 10)
## Each region that contains 1 ship, will result in 4 recursive calls.
## 3 will return 0 because they do not contain a ship and 1 call will result in 4 more recursive calls
## because it does contain a ship.
## This process will repeat until we make a recursive call with the exact coordinates of the ship.

## space complexity: log_2 max(M, N)


class Solution:
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        # recursive function
        def divide_conquer(tr, bl):

            # base cases
            if tr.x < bl.x or tr.y < bl.y:
                return 0

            if tr.x == bl.x and tr.y == bl.y:
                return int(sea.hasShips(tr, bl))

            if not sea.hasShips(tr, bl):
                return 0

            x0, y0 = bl.x, bl.y
            x1, y1 = tr.x, tr.y
            x_m = (x0 + x1) // 2
            y_m = (y0 + y1) // 2

            return (
                divide_conquer(tr, Point(x_m + 1, y_m + 1))
                + divide_conquer(Point(x_m, y_m), bl)
                + divide_conquer(Point(x1, y_m), Point(x_m + 1, y0))
                + divide_conquer(Point(x_m, y1), Point(x0, y_m + 1))
            )

        return divide_conquer(topRight, bottomLeft)
