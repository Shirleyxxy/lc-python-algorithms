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
