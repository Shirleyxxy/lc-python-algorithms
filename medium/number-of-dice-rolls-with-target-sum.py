## Dynamic programming with memoization
## Relation: dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)

## Time Complexity:  O(d * f * target)
## Space Complexity: O(d * target)

class Solution:
    def numRollsToTarget(self, d, f, target):
        '''
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        '''
        memo = {}
        def count(num_dice, target):
            if target > num_dice * f: return 0
            if target < 0: return 0
            if num_dice == 0: return target == 0
            if (num_dice, target) in memo: return memo[(num_dice, target)]

            num_rolls = 0
            for val in range(1, f+1):
                num_rolls += count(num_dice - 1, target - val)
            memo[(num_dice, target)] = num_rolls % (10**9+7)
            return memo[(num_dice, target)]

        return count(d, target)


class Solution:
    def numRollsToTarget(self, d, f, target):
        '''
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        '''
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp[0][0] = 1
        mod = 10**9+7
        for i in range(d+1):
            for t in range(1, target+1):
                for val in range(1, min(f, t)+1):
                    dp[i][t] = (dp[i][t] + dp[i-1][t-val]) % mod
        return dp[d][target]


class Solution:
    def numRollsToTarget(self, d, f, target):
        '''
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        '''
        dp = [[0] * (target+1) for _ in range(d+1)]
        dp[0][0] = 1
        mod = 10**9+7
        for i in range(1, d+1):
            for t in range(1, target+1):
                for val in range(1, f+1):
                    if val > t: break
                    dp[i][t] = (dp[i][t] + dp[i-1][t-val]) % mod
        return dp[d][target]
