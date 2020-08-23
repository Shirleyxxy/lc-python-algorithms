## Solution 1 - Stack
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def calculate(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        stack = []
        # res: on-going result
        # sign: 1 means positive, -1 means negative
        operand, res, sign = 0, 0, 1

        for ch in s:
            # operand could be more than one digit
            if ch.isdigit():
                operand = 10 * operand + int(ch)
            elif ch in '+-':
                # evaluate the expression
                res += sign * operand
                # reset operand and sign
                operand = 0
                sign = 1 if ch == '+' else -1
            # push the result and sign onto the stack
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                # reset sign and result for the new sub-expression
                sign, res = 1, 0
            elif ch == ')':
                # evaluate the sub-expression
                res += sign * operand
                # ')' marks the end of the expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop()
                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis)).
                res += stack.pop()
                operand = 0
        return res + sign * operand


## Solution 2 - Recursion & Stack
## Time Complexity: O(N)
## Space Complexity: O(N)

## popleft() in deque is much faster than pop(0) for the default list
from collections import deque

class Solution:
    def calculate(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        def calc_rec(ls):
            stack = []
            num, sign = 0, '+'
            while len(ls) > 0:
                ch = ls.popleft()
                if ch.isdigit():
                    num = 10 * num + int(ch)
                # do recursion to calculate the sum within the next (...)
                if ch == '(':
                    num = calc_rec(ls)
                if ch in '+-)' or len(ls) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    num, sign = 0, ch
                    # end the current recursion (calculation for the sub-expression), return the result
                    if ch == ')': break
            return sum(stack)

        return calc_rec(deque(list(s)))
