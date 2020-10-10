## Time Complexity: O(N)
## Space Complexity: O(N)
## Assume there are no invalid operations.

class Solution:
    def calPoints(self, ops):
        '''
        :type ops: List[str]
        :rtype: int
        '''
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)
