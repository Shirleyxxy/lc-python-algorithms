## Bottom-up 2D DP
## dp[i][j] - the min difficulty we get if we want to complete first j jobs using exact i days
## Time: O(N*N*d)
## Space: O(N*d)

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        '''
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        '''
        njobs = len(jobDifficulty)
        if njobs < d: return -1

        dp = [[float('inf')] * njobs for _ in range(d)]
        # base case - complete first j jobs using 1 day
        for j in range(njobs):
            dp[0][j] = max(jobDifficulty[:j+1])

        for i in range(1, d):
            for j in range(i, njobs):
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] + max(jobDifficulty[k:j+1]))
        return dp[d-1][njobs-1]


## Top-down DP - much faster
## Time: O(N*N*d)
## Space: O(N*d)
from functools import lru_cache
class Solution:
    def minDifficulty(self, jobDifficulty, ndays):
        '''
        :type jobDifficulty: List[int]
        :type ndays: int
        :rtype: int
        '''
        njobs = len(jobDifficulty)
        if njobs < ndays: return -1

        @functools.lru_cache(None)
        def dfs(j, d):
            '''
            minDifficulty if we start work at j-th job with d days left.
            '''
            # if we have only one day, we have to do all the jobs left.
            if d == 1:
                return max(jobDifficulty[j:])
            res, maxd = float('inf'), 0
            for i in range(j, njobs-d+1):
                maxd = max(maxd, jobDifficulty[i])
                res = min(res, maxd + dfs(i+1, d-1))
            return res
        return dfs(0, ndays)
