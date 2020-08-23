## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def reverseWords(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        # each word is separated by single space; no extra space in the string
        return ' '.join([word[::-1] for word in s.split()])
