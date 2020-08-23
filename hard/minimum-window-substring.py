## Time Complexity: O(N + M)
## Space Complexity: O(M)

class Solution:
    def minWindow(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: str
        '''
        window_start, matched, substr_start = 0, 0, 0
        min_len = len(s) + 1
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            if s[window_end] in t_freq:
                t_freq[s[window_end]] -= 1
                # count every matching of a character
                if t_freq[s[window_end]] >= 0: matched += 1

            # shrink the window if we can
            while matched == len(t):
                if min_len > window_end - window_start + 1:
                    min_len = window_end - window_start + 1
                    substr_start = window_start

                if s[window_start] in t_freq:
                    # note that we could have redundant matching characters, therefore we'll
                    # decrement the matched count only when a useful occurrence of a matched
                    # character is going out of the window
                    if t_freq[s[window_start]] == 0: matched -= 1
                    t_freq[s[window_start]] += 1

                window_start += 1

        return '' if min_len > len(s) else s[substr_start:substr_start + min_len]
