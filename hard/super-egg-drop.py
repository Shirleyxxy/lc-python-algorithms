## K eggs, N floors
## Dynamic Programming
## dp[i][j]: minimum number of drops needed to find the critical floor **in the worst case**.
## i: the number of eggs left to drop
## j: the number of floors left to test

## Brute force DP (TLE)
## Time Complexity: O(kn^2)
## Space Complexity: O(kn)
class Solution:
    def superEggDrop(self, K, N):
        '''
        :type K: int
        :type N: int
        :rtype: int
        '''
        dp = [[float('inf')] * (N+1) for _ in range(K+1)]
        # base case
        for i in range(1, K+1):
            dp[i][0] = 0  # 0 floor, no drop needed
            dp[i][1] = 1  # 1 floor, 1 drop needed
        for j in range(1, N+1):
            dp[1][j] = j  # 1 egg, check each floor from 1 to j
        # state transition
        for i in range(2, K+1):
            for j in range(2, N+1):
                # floor k for the next drop
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[K][N]


## dp[i-1][k-1] will increase and dp[i][j-k] will decrease as k goes up from 1 to j
## To minimize the maximum of the two values, they should be as close as possible.
## To get the optimal k value for dp[i][j], we can do a binary search for k from 1 to j.
## Time Complexity: O(knlogn)
## Space Complexity: O(kn)

class Solution:
    def superEggDrop(self, K, N):
        '''
        :type K: int
        :type N: int
        :rtype: int
        '''
        memo = {}
        def dp(K, N):
            if K == 1: return N # 1 egg
            if N == 0: return 0 # 0 floor
            if N == 1: return 1 # 1 floor
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('inf')
            # binary search
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                # res = min(max(broken, not broken) + 1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[(K, N)] = res
            return res
        return dp(K, N)


## Further Optimization:
## No need to search for k; the optimal floor k for each dp[i][j] increases as j increases
## In the third for loop, k will go from 1 to N only once as j in the second for loop goes from 1 to N.

## Time Complexity: O(kn)
## Space Complexity: O(kn)
class Solution:
    def superEggDrop(self, K, N):
        '''
        :type K: int
        :type N: int
        :rtype: int
        '''
        dp = [[float('inf')] * (N+1) for _ in range(K+1)]
        # base case
        for i in range(1, K+1):
            dp[i][0] = 0  # 0 floor, no drop needed
            dp[i][1] = 1  # 1 floor, 1 drop needed
        for j in range(1, N+1):
            dp[1][j] = j  # 1 egg, check each floor from 1 to j
        # state transition
        for i in range(2, K+1):
            k = 1
            for j in range(2, N+1):
                while k < j+1 and dp[i-1][k-1] < dp[i][j-k]:
                    k += 1
                dp[i][j] = 1 + dp[i-1][k-1]
        return dp[K][N]


## Optimization: a different state transition
## m drops allowed, k eggs
## dp[m][k]: the maximum number of floors we can check in the worst case
## example: dp[7][1] = 7

## total # floors = # floors above (if not broken) + # floors below (if broken) + 1 (current floor)
## dp[m][k] = dp[m-1][k] + dp[m-1][k-1] + 1

## Time Complexity: O(kn)
## Space Complexity: O(kn)
class Solution:
    def superEggDrop(self, K, N):
        '''
        :type K: int
        :type N: int
        :rtype: int
        '''
        dp = [[0] * (K+1) for _ in range(N+1)]
        for m in range(1, N+1):
            for k in range(1, K+1):
                dp[m][k] = dp[m-1][k] + dp[m-1][k-1] + 1
            if dp[m][K] >= N: return m
