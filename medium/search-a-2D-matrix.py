## Time Complexity: O(log(M*N))
## Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        '''
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        '''
        if not matrix: return False
        nrow, ncol = len(matrix), len(matrix[0])
        # binary search
        start, end = 0, nrow * ncol - 1
        while start <= end:
            mid = start + (end - start) // 2
            # find the key number using the index 
            num = matrix[mid//ncol][mid%ncol]
            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
