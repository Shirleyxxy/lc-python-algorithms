## Two pointers, sliding window, hash table
## Time Complexity: O(n)
## Space Complexity: O(k) for the sliding window, where k is the size of the set
## (number of unique characters).

class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        start, max_len = 0, 0
        used_d = {}
        for idx, char in enumerate(s):
            # update the start index
            if char in used_d and start <= used_d[char]:
                start = used_d[char] + 1
            # update max_len
            else:
                max_len = max(max_len, idx - start + 1)
            used_d[char] = idx
        return max_len
