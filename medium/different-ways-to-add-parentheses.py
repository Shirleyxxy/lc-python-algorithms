## Divide and Conquer
## Time Complexity: O(N * 2^N)
## Space Complexity: O(N * 2^N)

class Solution:
    def diffWaysToCompute(self, input):
        '''
        :type input: str
        :rtype: List[int]
        '''
        result = []
        if input.isdigit():
            result.append(int(input))
        for i, s in enumerate(input):
            if s in '+-*':
                # break into parts and make recursive calls
                left_vals = self.diffWaysToCompute(input[:i])
                right_vals = self.diffWaysToCompute(input[i+1:])
                for left in left_vals:
                    for right in right_vals:
                        result.append(self.calculate(left, right, s))
        return result

    def calculate(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        else:
            return a * b


## Divide and Conquer with Memoization
## Our recursive calls can be evaluating the same sub-expression multiple times.
class Solution:
    def diffWaysToCompute(self, input):
        return self.diffWaysToComputeRec(input, {})
    
    def diffWaysToComputeRec(self, input, memo):
        '''
        :type input: str
        :rtype: List[int]
        '''
        result = []
        if input.isdigit():
            result.append(int(input))

        if input in memo:
            return memo[input]

        for i, s in enumerate(input):
            if s in '+-*':
                # break into parts and make recursive calls
                left_vals = self.diffWaysToComputeRec(input[:i], memo)
                right_vals = self.diffWaysToComputeRec(input[i+1:], memo)
                for left in left_vals:
                    for right in right_vals:
                        result.append(self.calculate(left, right, s))
        return result

    def calculate(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        else:
            return a * b
