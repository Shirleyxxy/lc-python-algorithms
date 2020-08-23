## Solution 1
## Time Complexity: O(1)
## Space Complexity: O(1)
class Solution:
    def romanToInt(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res + roman[s[-1]]


## Solution 2
## Time Complexity: O(1) - As there is a finite set of roman numerals, the maximum number
## possible is 3999, which in roman numerals is MMMCMXCIX.
## Space Complexity: O(1)
class Solution:
    def romanToInt(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        res, i = 0, 0
        while i < len(s):
            if i < len(s)-1 and s[i:i+2] in roman:
                res += roman[s[i:i+2]]
                i += 2
            else:
                res += roman[s[i]]
                i += 1
        return res
