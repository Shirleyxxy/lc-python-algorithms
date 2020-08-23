class Solution:
    def balancedStringSplit(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        balance, res = 0, 0
        for char in s:
            balance += (char == 'R')
            balance -= (char == 'L')
            if balance == 0:
                res += 1
        return res 
