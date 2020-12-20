## My solution
class Solution:
    def generate(self, numRows):
        '''
        :type numRows: int
        :rtype: List[List[int]]
        '''
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for row in range(2, numRows):
            res.append([1] + [sum(res[-1][i:i+2]) for i in range(row-1)] + [1])
        return res


## A better solution
## Any row can be constructed using the offset sum of the previous row
##   1 3 3 1 0
## + 0 1 3 3 1
## = 1 4 6 4 1
class Solution:
    def generate(self, numRows):
        '''
        :type numRows: int
        :rtype: List[List[int]]
        '''
        res = [[1]]
        for i in range(1, numRows):
            res.append(list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])))
        return res if numRows else []


## Another clean solution
class Solution:
    def generate(self, numRows):
        '''
        :type numRows: int
        :rtype: List[List[int]]
        '''
        res = [[1] * (i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
        
