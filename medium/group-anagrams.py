## Solution 1 - Categorize by sorted string
## Time Complexity: O(NKlogK)
## The outer loop has O(N) as we iterate through each string.
## Then we sort each string in O(KlogK) time.
## K is the maximum length of a string in strs.
## Space Complexity: O(NK)
class Solution:
    def groupAnagrams(self, strs):
        '''
        :type strs: List[str]
        :rtype: List[List[str]]
        '''
        res = collections.defaultdict(list)
        for s in strs:
            # tuple is immutable and can be used as dictionary keys
            res[tuple(sorted(s))].append(s)
        return res.values()



## Solution 2 - Categorize by count
## Time Complexity: O(NK)
## Space Complexity: O(NK)
class Solution:
    def groupAnagrams(self, strs):
        '''
        :type strs: List[str]
        :rtype: List[List[str]]
        '''
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                # the ord() function returns an integer
                # representing the unicode character
                # ord('a') == 97
                count[ord(ch) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
