## Time: O(N) - IN operator
## Space: O(N) - keep s + s


class Solution:
    def repeatedSubstringPattern(self, s):
        '''
        :type s: str
        :rtype: bool

        PatternPattern
        PatternPatternPatternPattern
        *atternPatternPatternPatter*
        '''
        # if the new string contains the input string, the input string is
        # a repeated pattern string
        return s in (s + s)[1:-1]
