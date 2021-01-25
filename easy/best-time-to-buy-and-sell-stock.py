## One pass solution (Greedy)
## Time Complexity: O(N) - a single pass
## Space Complexity: O(1) - only 2 variables
class Solution:
    def maxProfit(self, prices):
        '''
        :type prices: List[int]
        :rtype: int
        '''
        # corner case
        if len(prices) <= 1: return 0
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit
