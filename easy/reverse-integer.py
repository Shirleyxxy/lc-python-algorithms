class Solution:
    def reverse(self, x):
        '''
        :type x: int
        :rtype: int
        '''
        sign = [1, -1][x < 0]
        rev = sign * int(str(abs(x))[::-1])
        return rev if -(2**31) <= rev <= (2**31)-1 else 0


## Time Complexity: O(logX)
## There are roughly log_10(X) digits in x 
## Space Complexity: O(1)
class Solution:
    def reverse(self, x):
        '''
        :type x: int
        :rtype: int
        '''
        sign = [1, -1][x < 0]
        rev, n = 0, abs(x)
        while n > 0:
            n, mod = divmod(n, 10)
            rev = rev * 10 + mod
        return sign*rev if -(2**31) <= sign*rev <= (2**31)-1 else 0
