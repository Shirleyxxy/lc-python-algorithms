## Implements pow(x, n), which calculates x raised to the power n.

## Brute Force Solution: Time Limit Exceeded
class Solution:
    def myPow(self, x, n):
        '''
        :type x: float
        :type n: int
        :rtype: float
        '''
        if n == 0: return 1
        res = 1
        if n > 0:
            for i in range(n):
                res = res * x
        if n < 0:
            for i in range(-n):
                res = res * (1/x)
        return res


## Recursion
## Time Complexity: O(logn)
## Space Complexity: O(logn) - for each computation, we need to store the result
## of x^(n/2). We need to do the computation O(logn) times.

class Solution:
    def myPow(self, x, n):
        '''
        :type x: float
        :type n: int
        :rtype: float
        '''
        if n == 0: return 1
        if n < 0: return 1.0 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        # even
        if n % 2 == 0:
            return half * half
        # odd
        else:
            return half * half * x
