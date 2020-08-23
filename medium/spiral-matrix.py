## Time Complexity: O(N)
## Space Complexity: O(1) without considering the output array
## O(N) if the output array is taken into account

class Solution:
    def spiralOrder(self, matrix):
        '''
        :type matrix: List[List[int]]
        :rtype: List[int]
        '''
        res = []
        if not matrix: return res
        row_s, col_s = 0, 0
        row_e, col_e = len(matrix), len(matrix[0])
        while row_s < row_e and col_s < col_e:
            for i in range(col_s, col_e):
                res.append(matrix[row_s][i])
            row_s += 1

            for j in range(row_s, row_e):
                res.append(matrix[j][col_e-1])
            col_e -= 1

            if row_s < row_e:
                for i in range(col_e-1, col_s-1, -1):
                    res.append(matrix[row_e-1][i])
                row_e -= 1

            if col_s < col_e:
                for j in range(row_e-1, row_s-1, -1):
                    res.append(matrix[j][col_s])
                col_s += 1
        return res


## better solution
class Solution:
    def spiralOrder(self, matrix):
        '''
        :type matrix: List[List[int]]
        :rtype: List[int]
        '''
        res = []
        if not matrix: return res
        nrows, ncols = len(matrix), len(matrix[0])
        row_s, row_e, col_s, col_e = 0, nrows-1, 0, ncols-1
        while row_s < row_e and col_s < col_e:
            res.extend([matrix[row_s][i] for i in range(col_s, col_e)])
            res.extend([matrix[j][col_e] for j in range(row_s, row_e)])
            res.extend([matrix[row_e][i] for i in range(col_e, col_s, -1)])
            res.extend([matrix[j][col_s] for j in range(row_e, row_s, -1)])
            row_s, row_e, col_s, col_e = row_s+1, row_e-1, col_s+1, col_e-1
        if row_s == row_e:
            res.extend([matrix[row_s][i] for i in range(col_s, col_e+1)])
        elif col_s == col_e:
            res.extend([matrix[j][col_s] for j in range(row_s, row_e+1)])
        return res
