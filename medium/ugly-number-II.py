## Idea
## An ugly number must be multiplied by either 2, 3, 5 from a smaller ugly number.
## Time Complexity: ~O(1) to retrieve preliminary computed ugly numbers, and about
## 1690 * 5 = 8450 operations for preliminary computations
## Space Complexity: ~O(1) to keep an array of 1690 ugly numbers

class Solution:
    def nthUglyNumber(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)

        return ugly[-1]
