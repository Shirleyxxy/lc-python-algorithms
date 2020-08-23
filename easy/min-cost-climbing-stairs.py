## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def minCostClimbingStairs(self, cost):
        '''
        :type cost: List[int]
        :rtype: int
        '''
        if not cost: return 0
        if len(cost) == 1: return cost[0]
        # dp[i]: min cost at the i-th step
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # the last step might come from either of the last two stairs
        return min(dp[-1], dp[-2])
