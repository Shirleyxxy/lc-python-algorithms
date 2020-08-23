## Dynamic Programming
## One can reach ith step in one of the two ways:
## 1. Taking a single step from (i-1)th step
## 2. Taking a step of 2 from (i-2)th step
## Let dp[i] denotes the number of ways to reach the ith step.
## dp[i] = dp[i-1] + dp[i-2]

## Updated Bottom-up solution
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def climbStairs(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        if n == 0: return 1
        if n <= 2: return n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

## Bottom up solution 1
## Time Complexity: O(n) - single loop up to n.
## Space Complexity: O(n) - array of size n.
class Solution:
    def climbStairs(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        res = [1, 2] # n=1, n=2
        for i in range(2, n):
            res.append(res[i-1] + res[i-2])
        return res[n-1]


## Bottom up solution 2
## Time Complexity: O(n) - single loop up to n is required to calculate nth Fibonacci number.
## Space Complexity: O(1) - no array, constant space is used.
class Solution:
    def climbStairs(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b


## Top down solution 3
## Recursion
## Time Limit Exceeded!
class Solution:
    def climbStairs(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
