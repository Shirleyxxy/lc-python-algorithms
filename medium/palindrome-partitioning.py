## Backtracking patterns: Choice (Snippet to recurse on) + Constraints + Goal
## Time Complexity: O(N * 2^N)
## Worst Case: 'aaaa' n-repetitions
## Space Complexity: O(N) call stack

class Solution:
    ## driver function
    def partition(self, s):
        '''
        :type s: str
        :rtype: List[List[str]]
        '''
        res = [] # for all the valid decompositions
        self.decompose(s, [], res) # [] is for the current decomposition we're working on
        return res

    def decompose(self, s, curr, res):
        # goal: decompose the entire string
        # the pointer runs over (out of bounds)
        if not s:
            res.append(curr[:]) # make a copy
            # return
        # backtracking
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                # decomposition in progress
                curr.append(s[:i])
                self.decompose(s[i:], curr, res)
                # go back to the call stack
                curr.pop()

    def isPalindrome(self, s):
        return s == s[::-1]
