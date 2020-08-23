## Bottom-up DP
## Time Complexity: O(N^2)
## Space Complexity: O(N^2)

class Solution:
    def minCut(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        is_palindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        # every string with one character is a palindrome
        for i in range(len(s)):
            is_palindrome[i][i] = True

        for start_idx in range(len(s)-1, -1, -1):
            for end_idx in range(start_idx+1, len(s)):
                if s[start_idx] == s[end_idx]:
                    # if it's a two character string or if the remaining string is a palindrome too
                    if end_idx - start_idx == 1 or is_palindrome[start_idx+1][end_idx-1]:
                        is_palindrome[start_idx][end_idx] = True

        # every index in 'cuts' stores the minimum cuts needed
        # for the substring from that index till the end
        cuts = [0 for _ in range(len(s))]
        for start_idx in range(len(s)-1, -1, -1):
            min_cuts = len(s)-1
            for end_idx in range(len(s)-1, start_idx-1, -1):
                if is_palindrome[start_idx][end_idx]:
                    min_cuts = 0 if end_idx == len(s)-1 else min(min_cuts, 1 + cuts[end_idx+1])
            cuts[start_idx] = min_cuts

        return cuts[0]
