## Dynamic Programming
## Time Complexity: O(m * n)
## Space Complexity: O(m * n)

## with one more addition row and one more additional column
class Solution:
    def maximalSquare(self, matrix):
        '''
        :type matrix: List[List[str]]
        :rtype: int
        '''
        if matrix is None or len(matrix) < 1: return 0
        # create a dp grid which has one additional row and column to facilitate computing
        # dp cells for first row and first column in matrix
        nrows, ncols = len(matrix), len(matrix[0])
        dp = [[0] * (ncols+1) for _ in range(nrows+1)]
        max_side = 0
        for row in range(nrows):
            for col in range(ncols):
                if matrix[row][col] == '1':
                    # be careful with the indexing since dp grid has additional row and column
                    dp[row+1][col+1] = min(dp[row][col], dp[row][col+1], dp[row+1][col]) + 1
                    max_side = max(max_side, dp[row+1][col+1])
        return max_side * max_side


## without one more additional row or column
class Solution:
    def maximalSquare(self, matrix):
        '''
        :type matrix: List[List[str]]
        :rtype: int
        '''
        ## matrix == [] or matrix == [[]]
        if not matrix or len(matrix[0]) == 0: return 0
        nrows, ncols = len(matrix), len(matrix[0])
        dp = [[0] * (ncols) for _ in range(nrows)]
        max_side = 0
        for row in range(nrows):
            for col in range(ncols):
                ## special case: first row / column
                if row == 0 or col == 0:
                    dp[row][col] = int(matrix[row][col])
                elif matrix[row][col] == '1':
                    dp[row][col] = min(dp[row-1][col-1], dp[row][col-1], dp[row-1][col]) + 1
                max_side = max(max_side, dp[row][col])
        return max_side * max_side
