## Time Complexity: O((N-L)*L)
## N = len(haystack), L = len(needle)
## Space Complexity: O(1)

class Solution:
    def strStr(self, haystack, needle):
        '''
        :type haystack: str
        :type needle: str
        :rtype: int
        '''
        for start in range(len(haystack) - len(needle) + 1):
            if haystack[start:start+len(needle)] == needle:
                return start
        return -1
