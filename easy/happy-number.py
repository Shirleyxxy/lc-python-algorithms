## Solution 1: Set
## Time Complexity: O(logN)
## Space Complexity: O(logN)

class Solution:
    def isHappy(self, n):
        '''
        :type n: int
        :rtype: boolean
        '''
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            n = sum([int(n)**2 for n in str(n)])
        return n == 1


## Solution 2: Fast & slow pointers
## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def isHappy(self, n):
        '''
        :type n: int
        :rtype: boolean
        '''
        def next_n(n):
            return sum([int(d)**2 for d in str(n)])

        slow, fast = n, n
        while True:
            slow = next_n(slow)
            fast = next_n(next_n(fast))
            if slow == fast: break
        return slow == 1
