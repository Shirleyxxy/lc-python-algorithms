## Recursion & Stack
## Time Complexity: O(N)
## Space Complexity: O(N)

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
                if ch == '(':
                    # do recursion to calculate the sum within the next (...)
                    num = calc_rec(ls)
                # start to evaluate the expression
                if ch in '+-/*)' or len(ls) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        # note: the integer division should truncate toward zero
                        # cannot use //
                        # compare -3 // 2 with int(-3 / 2)
                        stack.append(int(stack.pop() / num))
                    # reset the values for num, sign
                    num, sign = 0, ch
                    # break to end the current recursion
                    # return the sum within the parenthesis back to its parent who
                    # invoked the recursion 
                    if sign == ')': break
            return sum(stack)

        return calc_rec(deque(list(s)))
