## Time Complexity: O(1)
## The number of iterations is fixed since the integer is of fixed size (32 bits).
## Space Complexity: O(1)

class Solution:
    def reverseBits(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        # initialize to 0; in binary it's 32 zeros
        res = 0
        for i in range(32):
            # shift all the bits that we already have in the result to the left
            # then set the rightmost bit (0 at the time) to the value we got in (n & 1)
            # use (n & 1) to retrive the rightmost bit in an integer n, which is equivalent to (n % 2).
            res = (res << 1) + (n & 1)
            # iterate through the bit string of the input integer
            n = n >> 1
        return res
