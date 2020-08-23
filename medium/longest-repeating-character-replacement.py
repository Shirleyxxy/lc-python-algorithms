## Time Complexity: O(N) - N is the number of letters in the input string
## Space Complexity: O(26), asymptotically O(1)

class Solution:
    def characterReplacement(self, s, k):
        '''
        :type: s
        :type: k
        :rtype: int
        '''
        window_start, max_len, max_repeat_letter_cnt = 0, 0, 0
        freq_d = {}
        for window_end in range(len(s)):
            freq_d[s[window_end]] = freq_d.get(s[window_end], 0) + 1
            max_repeat_letter_cnt = max(max_repeat_letter_cnt, freq_d[s[window_end]])
            if window_end - window_start + 1 - max_repeat_letter_cnt > k:
                freq_d[s[window_start]] -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len
