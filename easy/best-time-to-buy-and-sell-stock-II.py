## Visualize the problem as calculating the upslopes
## a.k.a Sum the differences between the peaks and the valleys
## Upslopes can be broken down into summations of many smaller upslopes
## Keep on adding the difference between the consecutive numbers of the array
## if the second number is larger than the first one

## Time Complexity: O(n) - a single pass
## Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        '''
        :type prices: List[int]
        :rtype: int
        '''
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(prices[i] - prices[i-1], 0)
        return max_profit
