## Solution 1
## Slow & memory-intensive
class Solution:
    def lastRemaining(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        arr = range(1, n+1)
        while len(arr) > 1:
            arr = arr[1::2][::-1]
        return arr[0]


## Solution 2
## Recursion
class Solution:
    def lastRemaining(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))


## Solution 3
## Idea: update and record head in each round
## When the total number becomes 1, head is the only number left

## When will head be updated?
## if we move from left
## if we move from right and there are odd number of remaining elements
class Solution:
    def lastRemaining(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        step = 1
        head = 1
        remains = n
        left = True

        while remains > 1:
            if left or (remains % 2 == 1):
                head += step
            step *= 2
            remains //= 2
            left = not left
        return head
