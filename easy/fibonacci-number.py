## Bottom-up DP
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def fib(self, N):
        '''
        :type N: int
        :rtype: int
        '''
        if N < 2: return N
        dp = [0] * (N+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]


## Memory Optimization
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def fib(self, N):
        '''
        :type N: int
        :rtype: int
        '''
        if N < 2: return N
        a, b = 0, 1
        for i in range(2, N+1):
            a, b = b, a+b
        return b


##### Old Versions #####
## Recursion
class Solution:
    def fib(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)


## Top-down with memoization
class Solution:
    def __init__(self):
        self.memo = []
        self.memo.append(0)
        self.memo.append(1)

    def fib(self, N):
        if N < len(self.memo):
            return self.memo[N]
        else:
            for i in range(2, N+1):
                self.memo.append(self.memo[i-2] + self.memo[i-1])
        return self.memo[N]
