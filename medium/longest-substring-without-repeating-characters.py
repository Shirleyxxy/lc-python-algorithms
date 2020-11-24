## Sliding Window
## Time Complexity: O(N)
## Space Complexity: O(K) where K is the number of unique characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        start, max_len = 0, 0
        ch2idx = {}
        for idx, char in enumerate(s):
            # update the start index
            if char in ch2idx and start <= ch2idx[char]:
                start = ch2idx[char] + 1
            # update max_len
            else:
                max_len = max(max_len, idx - start + 1)
            ch2idx[char] = idx
        return max_len
