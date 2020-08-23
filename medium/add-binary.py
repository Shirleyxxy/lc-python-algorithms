## Solution 1: Built-in function
class Solution:
    def addBinary(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        return bin(int(a, 2) + int(b, 2))[2:]


## Solution 2: Addition principle
## Time Complexity: O(max(m, n)), where m and n are lengths of the input strings a and b
## Space Complexity: O(max(m, n))

class Solution:
    def addBinary(self, a, b):
        '''
        :type a: str
        :type b: str
        :rtype: str
        '''
        # make sure a and b are of the same length
        # if not, add '0' in front of the shorter binary string
        if len(a) < len(b):
            a, b = b, a
        diff = len(a) - len(b)
        b = '0' * diff + b

        res, carry = '', 0
        for i, j in zip(a[::-1], b[::-1]):
            sum = int(i) + int(j) + carry
            # update in the reverse order
            res = str(sum % 2) + res
            carry = sum // 2
        return '1' + res if carry == 1 else res
