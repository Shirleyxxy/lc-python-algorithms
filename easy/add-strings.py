## Similar problem:
## lc2 - add two numbers (linkedlists)
## lc67 - add binary
## Time Complexity: O(max(N1, N2))
## Space Complexity: O(max(N1, N2))

class Solution:
    def addStrings(self, num1, num2):
        '''
        Digit-by-digit addition.
        :type num1: str
        :type num2: str
        :rtype: str
        '''
        # set a pointer at the end of each string
        p1, p2 = len(num1)-1, len(num2)-1
        carry, res = 0, []
        # stop only when both strings are used entirely
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            carry, val = divmod(x1 + x2 + carry, 10)
            res.append(str(val))
            p1 -= 1; p2 -= 1
        # check if the carry is non-zero
        if carry > 0:
            res.append(str(carry))

        return ''.join(res[::-1])
