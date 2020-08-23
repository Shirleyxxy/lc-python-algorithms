## The representation uses the largest possible symbols from left to right.
## Greedy

## Time Complexity: O(1) since there is a finite set of values and the corresponding
## roman numerals to iterate through.
## Space Complexity: O(1) - the amount of memory used does not change with the size
## of the input integer
class Solution:
    def intToRoman(self, num):
        '''
        :type num: int
        :rtype: str
        '''
        # Sequences must be in order from largest to smallest
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''
        for val, sym in zip(values, symbols):
            res += (num // val) * sym
            num %= val
        return res
