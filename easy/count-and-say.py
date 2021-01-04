## Recursion
## Time Complexity: O(2^N)
## In the worst case, the next sequence would double the length and grow exponentially.
## Space Complexity: O(2^(N-1))
class Solution:
    def countAndSay(self, n):
        '''
        :type n: int
        :rtype: str
        '''
        # base case
        if n == 1: return '1'
        s = self.countAndSay(n-1)
        i, res = 0, ''
        while i < len(s):
            count = 1
            while i+1 < len(s) and s[i+1] == s[i]:
                count += 1
                i += 1
            res += str(count) + s[i]
            i += 1
        return res


## Similar idea (and complexity)
class Solution:
    def countAndSay(self, n):
        '''
        :type n: int
        :rtype: str
        '''
        res = '1'
        for _ in range(n-1):
            prev = res
            res, i = '', 0
            while i < len(prev):
                curr, count = prev[i], 1
                i += 1
                while i < len(prev) and prev[i] == curr:
                    count += 1
                    i += 1
                res += str(count) + curr
        return res
