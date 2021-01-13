## Recursion
## Time: O(N) in the worst case
## Space: O(1)
class Solution:
    def plusOne(self, digits):
        '''
        :type digits: List[int]
        :rtype: List[int]
        '''
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        return digits


## Note: The solutions below will work if the integer does not contain any leading zero
## Failed test case: [0, 0]
## Output: [1]
## Expected: [0, 1]
class Solution:
    def plusOne(self, digits):
        '''
        :type digits: List[int]
        :rtype: List[int]
        '''
        num = 0
        for i, digit in enumerate(digits):
            num += digit * pow(10, len(digits)-i-1)
        return [int(d) for d in str(num+1)]

## Same idea using built-in functions
class Solution:
    def plusOne(self, digits):
        '''
        :type digits: List[int]
        :rtype: List[int]
        '''
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))
