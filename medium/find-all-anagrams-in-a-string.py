## Time Complexity: O(N_s + N_p) since it's one pass along both strings.
## Space Complexity: O(1) since p_cnt and s_cnt contain not more than 26 elements.
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        '''
        :type s: str
        :type p: str
        :rtype: List[int]
        '''
        len_s, len_p = len(s), len(p)
        res = []
        p_cnt = Counter(p) # reference counter
        s_cnt = Counter()
        # sliding window
        for i in range(len_s):
            # add one more letter on the right side of the window
            s_cnt[s[i]] += 1
            # remove one letter from the left side of the window
            if i >= len_p:
                if s_cnt[s[i-len_p]] == 1:
                    del s_cnt[s[i-len_p]]
                else:
                    s_cnt[s[i-len_p]] -= 1
            if s_cnt == p_cnt:
                res.append(i-len_p+1)
        return res


## -------------------------------------
## Time Complexity: O(N + M)
## Space Complexity: O(M)
class Solution:
    def findAnagrams(self, s, p):
        '''
        :type s: str
        :type p: str
        :rtype: List[int]
        '''
        result_indices = []
        window_start, matched = 0, 0
        p_freq = {}
        for ch in p:
            p_freq[ch] = p_freq.get(ch, 0) + 1

        for window_end in range(len(s)):
            if s[window_end] in p_freq:
                p_freq[s[window_end]] -= 1
                if p_freq[s[window_end]] == 0: matched += 1

            if matched == len(p_freq): result_indices.append(window_start)

            if window_end >= len(p) - 1:
                if s[window_start] in p_freq:
                    if p_freq[s[window_start]] == 0: matched -= 1
                    p_freq[s[window_start]] += 1
                window_start += 1
        return result_indices
