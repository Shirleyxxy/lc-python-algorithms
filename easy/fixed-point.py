## Time: O(N)
class Solution:
    def fixedPoint(self, A):
        '''
        :type A: List[int]
        :rtype: int
        '''
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1

## We need to use the fact that A is a list of distinct integers
## sorted in ascending order.
## A[i] is distinct and ascending.
## A[i] - i is non-descending array.
## Binary search the first 0 in the array of A[i] - i.

## A[i] < A[i+1]
## A[i] <= A[i+1] - 1
## A[i] - i <= A[i+1] - (i+1)

## Time: O(logN)
class Solution:
    def fixedPoint(self, A):
        '''
        :type A: List[int]
        :rtype: int
        '''
        if not A: return -1
        start, end = 0, len(A)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] - mid >= 0:
                end = mid
            else:
                start = mid
        if A[start] == start: return start
        if A[end] == end: return end
        return -1
