## Brute force
## Time Complexity: O(M * N)
## Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        '''
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        '''
        for row in matrix:
            if target in row:
                return True
        return False


## Search space reduction
## Rows are sorted from left to right; columns are sorted from top to bottom
## Time Complexity: O(M + N)
## Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        '''
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # start the pointer in the bottom-left
        # similarly, we can also start from top-right corner
        row, col = len(matrix)-1, 0
        while col < len(matrix[0]) and row >= 0:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            # found the target
            else:
                return True
        return False
