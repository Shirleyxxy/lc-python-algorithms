## Time Complexity: O(|coins| * amount)
## Space Complexity: O(amount)

class Solution:
    def change(self, amount, coins):
        '''
        :type amount: int
        :type coins: List[int]
        :rtype: int
        '''
        dp = [1] + [0] * amount
        for coin in coins:
            for amt in range(1, amount+1):
                if amt >= coin:
                    dp[amt] += dp[amt-coin]
        return dp[amount]


## dp[i][amt]: the number of ways to get amount "amt" using the first i coins
## Time Complexity: O(|coins| * amount)
## Space Complexity: O(|coins| * amount)

class Solution:
    def change(self, amount, coins):
        '''
        :type amount: int
        :type coins: List[int]
        :rtype: int
        '''
        if len(coins) == 0: return int(amount == 0)
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        # there's one way to get amount = 0: do not take any coins
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range(len(coins)):
            for amt in range(1, amount+1):
                if i > 0:
                    dp[i][amt] = dp[i-1][amt]
                if amt >= coins[i]:
                    dp[i][amt] += dp[i][amt-coins[i]]
        return dp[-1][-1]
