## Dynamic Programming
## dp[i][j]: the minimum cost to paint all the way to house i using color j
## return min(dp[-1]) to find the minimum cost to paint all the houses

## Solution 1
## Time Complexity: O(n)
## Space Complexity: O(n*3) (for 3 colors in the problem)
class Solution:
    def minCost(self, costs):
        '''
        :type costs: List[List[int]]
        :rtype: int
        '''
        if not costs: return 0
        n, c = len(costs), len(costs[0])
        dp = [[0] * c for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            # paint house i using red
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            # paint house i using blue
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            # paint house i using green
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        return min(dp[-1])


## Solution 2
## Modify the original matrix
class Solution:
    def minCost(self, costs):
        '''
        :type costs: List[List[int]]
        :rtype: int
        '''
        if not costs: return 0
        for i in range(1, len(costs)):
            # paint house i using red
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            # paint house i using blue
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            # paint house i using green
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])


## Solution 3
## Follow-up: make the code work for any number of colors
class Solution:
    def minCost(self, costs):
        '''
        :type costs: List[List[int]]
        :rtype: int
        '''
        if not costs: return 0
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
        return min(costs[-1])


## Solution 4
## Space Complexity: O(1)
class Solution:
    def minCost(self, costs):
        '''
        :type costs: List[List[int]]
        :rtype: int
        '''
        if not costs: return 0
        res = costs[0]
        for i in range(1, len(costs)):
            pre = res[:]
            # paint house i using red
            res[0] = costs[i][0] + min(pre[1], pre[2])
            # paint house i using blue
            res[1] = costs[i][1] + min(pre[0], pre[2])
            # paint house i using green
            res[2] = costs[i][2] + min(pre[0], pre[1])
        return min(res)


## Solution 5
## Space Complexity: O(1)
## Follow-up: make the code work for any number of colors
class Solution:
    def minCost(self, costs):
        '''
        :type costs: List[List[int]]
        :rtype: int
        '''
        if not costs: return 0
        res = costs[0]
        for i in range(1, len(costs)):
            pre = res[:]
            for j in range(len(costs[0])):
                res[j] = costs[i][j] + min(pre[:j] + pre[j+1:])
        return min(res)
