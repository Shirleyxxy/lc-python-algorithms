## Stack
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def calculate(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        # num: buffer for the operand since it can have more than 1 digit
        # prev_sign: buffer for the last sign
        num, stack, prev_sign = 0, [], '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            # start to evaluate the expression
            if s[i] in '+-*/' or i == len(s)-1:
                if prev_sign == '+':
                    stack.append(num)
                if prev_sign == '-':
                    stack.append(-num)
                if prev_sign == '*':
                    stack.append(stack.pop() * num)
                if prev_sign == '/':
                    # the integer division should truncate toward zero
                    stack.append(int(stack.pop() / num))
                # reset the values for num, prev_sign
                num = 0
                prev_sign = s[i]
        return sum(stack)
