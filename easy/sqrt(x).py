## Note1: x is guaranteed to be a non-negative integer.
## Note2: Integers are implemented as "long" integer objects of arbitrary size in Python3
## and do not normally overflow.

## Binary Search
## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def mySqrt(self, x):
        '''
        :type x: int
        :rtype: int
        '''
        if x < 2: return x
        start, end = 0, x
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
