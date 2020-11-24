## Recursive Solution
## Time Complexity: O(3^N * 4^M)
## Space Complexity: O(3^N * 4^M)
## N is the number of digits in the input that maps to 3 letters
## M is the number of digits in the input that maps to 4 letters
## N + M is the total number of digits in the input

class Solution:
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        if not digits: return []
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 1:
            return list(mapping[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        final = mapping[digits[-1]]
        return [p + c for p in prev for c in final]


## Iterative Solution
## Time Complexity: O(3^N * 4^M)
## Space Complexity: O(3^N * 4^M)
class Solution:
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = [''] if digits else []
        for d in digits:
            curr = []
            for p in res:
                for c in mapping[d]:
                    curr.append(p + c)
            res = curr
        return res


## Further simplified version
class Solution:
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = [''] if digits else []
        for d in digits:
            res = [p + c for p in res for c in mapping[d]]
        return res


## Bottom-up Backtracking (more explicit)
## Time Complexity: O(3^N * 4^M)
## Space Complexity: O(3^N * 4^M)
class Solution:
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []

        def backtracking(i, curr):
            if i == len(digits):
                if len(curr) > 0:
                    res.append(curr)
                return

            for ch in mapping[digits[i]]:
                curr += ch
                backtracking(i+1, curr)
                curr = curr[:-1]

        backtracking(0, '')
        return res


## My solution (backtracking)
class Solution:
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        self.digits = digits
        # digit-to-letter mapping
        self.mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.res = []
        self.backtracking(0, '')
        return self.res

    def backtracking(self, i, curr):
        if i == len(self.digits):
            if len(curr) > 0:
                self.res.append(curr[:])
        else:
            for ch in self.mapping[self.digits[i]]:
                curr += ch
                self.backtracking(i+1, curr)
                curr = curr[:-1]


## Pathrise HackerRank
class Solution:
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        if not digits: return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        curr = []
        def backtracking(i):
            if i == len(digits):
                res.append(''.join(curr[:]))
            else:
                for ch in mapping[digits[i]]:
                    curr.append(ch)
                    backtracking(i+1)
                    curr.pop()
        backtracking(0)
        return sorted(res)
