## Time Complexity: O(N^2)
## Space Complexity: O(N)
class Solution:
    def validWordSquare(self, words):
        '''
        :type words: List[str]
        :rtype: bool
        '''
        for i, row in enumerate(words):
            col = ''
            for word in words:
                try:
                    col += word[i]
                except:
                    break
            if row != col:
                return False
        return True


## Python trick:
from itertools import zip_longest
class Solution:
    def validWordSquare(self, words):
        '''
        :type words: List[str]
        :rtype: bool
        '''
        return words == [''.join(filter(None, word)) for word in zip_longest(*words)]


## Test case:
words = ['abcd', 'bnrt', 'crm', 'dt']
list(zip(*words))
list(zip_longest(*words))
