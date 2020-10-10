## Note:
## 1. zero "0" is a single digit but it doesn't have any mapping by itself.
## 2. At any given point we either decode using two digits or single digit.
## 3. The trick is to set up the base case correctly.

## Dynamic Programming
## dp[i] = number of ways of decoding substring s[:i]
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def numDecodings(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        if not s: return 0
        dp = [0] * (len(s) + 1)
        # base case
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):
            # one-digit jump
            # if s[i-1] is a valid single digit decode
            # thus whatever is in dp[i-1] we add to dp[i].
            # if there are N ways of reaching dp[i-1], now
            # those N ways also lead to dp[i].
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            # two-digit jump
            # if the two digit decoding is valid
            # we add dp[i-2] to dp[i].
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]
