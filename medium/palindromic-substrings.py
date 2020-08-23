## Bottom-up DP
## Time Complexity: O(N^2)
## Space Complexity: O(N^2)

class Solution:
    def countSubstrings(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0

        for i in range(len(s)):
            dp[i][i] = True
            count += 1

        for start_idx in range(len(s)-1, -1, -1):
            for end_idx in range(start_idx+1, len(s)):
                if s[start_idx] == s[end_idx]:
                    if end_idx - start_idx == 1 or dp[start_idx+1][end_idx-1]:
                        dp[start_idx][end_idx] = True
                        count += 1
        return count
