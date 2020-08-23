## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def sortedSquares(self, A):
        '''
        :type A: List[int]
        :rtype: List[int]
        '''
        squares = [0] * len(A)
        left, right, curr_idx = 0, len(A)-1, len(A)-1
        while left <= right:
            if A[left] ** 2 > A[right] ** 2:
                squares[curr_idx] = A[left] ** 2
                left += 1
            else:
                squares[curr_idx] = A[right] ** 2
                right -= 1
            curr_idx -= 1
        return squares
