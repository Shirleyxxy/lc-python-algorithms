## My solution using zip(*iterables)
class Solution:
    def longestCommonPrefix(self, strs):
        '''
        :type strs: List[str]
        :rtype: str
        '''
        prefix = ''
        for el in zip(*strs):
            if len(set(el)) == 1:
                prefix += el[0]
            else:
                return prefix
        return prefix


## Similar idea; slightly different code
class Solution:
    def longestCommonPrefix(self, strs):
        '''
        :type strs: List[str]
        :rtype: str
        '''
        if not strs: return ''
        shortest = min(strs, key = len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
