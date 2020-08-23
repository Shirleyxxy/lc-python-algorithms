## Time Complexity: O(N * 2^N)
## Space Complexity: O(N * 2^N)

class Solution:
    def letterCasePermutation(self, S):
        '''
        :type S: str
        :rtype: List[str]
        '''
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [perm + s for perm in res for s in [ch.upper(), ch.lower()]]
            else:
                res = [perm + ch for perm in res]
        return res
