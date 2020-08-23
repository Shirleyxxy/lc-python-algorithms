## Time Complexity: O(N + M) - N and M are the number of characters in the input string s2 and the pattern s1.
## Space Complexity: O(M) - in the worst case, the whole pattern s1 can have distinct characters which all go into the dictionary.

class Solution:
    def checkInclusion(self, s1, s2):
        '''
        :type s1: str
        :type s2: str
        :rtype: bool
        '''
        window_start, matched = 0, 0
        s1_d = {}
        for ch in s1:
            s1_d[ch] = s1_d.get(ch, 0) + 1

        for window_end in range(len(s2)):
            if s2[window_end] in s1_d:
                s1_d[s2[window_end]] -= 1
                if s1_d[s2[window_end]] == 0: matched += 1

            if matched == len(s1_d): return True

            if window_end >= len(s1) - 1:
                if s2[window_start] in s1_d:
                    if s1_d[s2[window_start]] == 0: matched -= 1
                    s1_d[s2[window_start]] += 1
                window_start += 1
        return False
