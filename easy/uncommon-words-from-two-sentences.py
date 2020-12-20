## A and B both contain only spaces and lowercase letters
## A word is uncommon if it appears exactly once in one of the sentences, and does not appear
## in the other sentence.
## Return the list in any order

## My Solution
## Time Complexity: O(M + N)
## Space Complexity: O(M + N)
class Solution:
    def uncommonFromSentences(self, A, B):
        '''
        :type A: str
        :type B: str
        :rtype: List[str]
        '''
        A_ls = A.split()
        B_ls = B.split()
        counter = {}
        for word in A_ls:
            counter[word] = counter.get(word, 0) + 1
        for word in B_ls:
            counter[word] = counter.get(word, 0) + 1
        res = []
        for w, cnt in counter.items():
            if cnt == 1:
                res.append(w)
        return res



## Same idea, optimized code
class Solution:
    def uncommonFromSentences(self, A, B):
        '''
        :type A: str
        :type B: str
        :rtype: List[str]
        '''
        counter = collections.Counter((A + ' ' + B).split())
        return [w for w in counter if counter[w] == 1]
