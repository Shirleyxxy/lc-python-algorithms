# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

## Idea: with each call to knows(...)
## We can conclusively determine that exactly 1 of the people is not a celebrity.
## knows(A, B) returns True --> A is not a celebrity
## knows(A, B) returns False --> B is not a celebrity

## Step 1: Narrow the people down to a single celebrity candidate
## Step 2: Check whether or not that candidate is a celebrity

## Time Complexity: O(N + N) = O(N)
## Space Complexity: O(1)
class Solution:
    def findCelebrity(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        self.n = n
        candidate = 0
        ########################
        # find a celebrity candidate
        # this requires (n-1) calls
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        ########################

        if self.is_celebrity(candidate):
            return candidate
        return -1


    def is_celebrity(self, i):
        '''
        Checks whether or not the given person i is a celebrity.
        O(N) time complexity.
        '''
        for j in range(self.n):
            if j == i: continue
            if knows(i, j) or not knows(j, i): return False
        return True



## Another elegant solution
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def findCelebrity(self, n):
        '''
        :type n: int
        :rtype: int
        '''
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        if any(knows(candidate, i) for i in range(candidate)):
            return -1
        if any(not knows(i, candidate) for i in range(n)):
            return -1
        return candidate
