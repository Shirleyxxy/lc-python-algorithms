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
