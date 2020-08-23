## You are given coins of different denominations and a total amount of money amount.
## Write a function to compute the fewest number of coins that you need to make up that amount.
## If that amount of money cannot be made up by any combination of the coins, return -1.

## Time Complexity: O(amount * len(coins))
## Space Complexity: O(amount)

## Bottom up DP
class Solution:
    def coinChange(self, coins, amount):
        '''
        :type coins: List[int]
        :type amount: int
        :rtype: int
        '''
        dp = [0] + [float('inf')] * amount
        for amt in range(1, amount+1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

## DP (slightly better)
class Solution:
    def coinChange(self, coins, amount):
        '''
        :type coins: List[int]
        :type amount: int
        :rtype: int
        '''
        dp = [0] + [float('inf')] * amount
        for amt in range(1, amount+1):
            dp[amt] = min(dp[amt-coin] if amt-coin >= 0 else float('inf') for coin in coins) + 1
        return dp[amount] if dp[amount] != float('inf') else -1
