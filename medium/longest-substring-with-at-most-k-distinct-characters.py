## Sliding Window
## Given a string, find the length of the longest substring T that contains at most k distinct characters.
## Time Complexity: O(N) - N is the number of characters in the input string
## Space Complexity: O(K) - We will be storing a maximum of K+1 characters in the dictionary
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        '''
        :type s: str
        :type k: int
        :rtype: int
        '''
        max_len, window_start = 0, 0
        char_freq = {}
        for window_end in range(len(s)):
            char_freq[s[window_end]] = char_freq.get(s[window_end], 0) + 1
            while len(char_freq) > k:
                char_freq[s[window_start]] -= 1
                if char_freq[s[window_start]] == 0: del char_freq[s[window_start]]
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len
