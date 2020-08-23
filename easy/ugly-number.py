## Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def isUgly(self, num):
        '''
        :type num: int
        :rtype: bool
        '''
        if num <= 0: return False

        for pf in [2, 3, 5]:
            while num % pf == 0:
                num //= pf
        return num == 1
