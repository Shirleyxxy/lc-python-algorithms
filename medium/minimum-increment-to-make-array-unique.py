## Solution 1 - Sort the array then increment one by one
## Time Complexity: O(NlogN)
## Space Complexity: ~ O(N) depends on the sorting algorithm used
class Solution:
    def minIncrementForUnique(self, A):
        '''
        :type A: List[int]
        :rtype: int
        '''
        A.sort()
        increments = 0
        if len(A) < 2: return 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                increments += A[i-1] + 1 - A[i]
                A[i] = A[i-1] + 1
        return increments


## Solution 2 - Counter / Dictionary
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def minIncrementForUnique(self, A):
        '''
        :type A: List[int]
        :rtype: int
        '''
        if not A: return 0
        counter = collections.Counter(A)
        stack = [] # store elements to increment
        diff = 0
        for k in range(min(counter.keys()), max(counter.keys())+1):
            if k in counter:
                stack += [k] * (counter[k] - 1)
            elif k not in counter and stack:
                diff += k - stack.pop()
        return diff + sum(range(k+1, k+1+len(stack))) - sum(stack)
