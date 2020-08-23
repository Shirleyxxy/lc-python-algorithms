## Clockwise Rotation
## Turn it upside down, then flip it across the diagonal (swap the symmetric elements)
## Time Complexity: O(N^2)
## Space Complexity: O(1)

class Solution:
    def rotate(self, matrix):
        '''
        Do not return anything, modify matrix in-place instead.
        :type matrix: List[List[int]]
        :rtype: None
        '''
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


## Anti-clockwise Rotation
## Flip it across the diagonal (swap the symmetric elements), then turn it upside down.
## Time Complexity: O(N^2)
## Space Complexity: O(1)

class Solution:
    def rotate(self, matrix):
        '''
        Do not return anything, modify matrix in-place instead.
        :type matrix: List[List[int]]
        :rtype: None
        '''
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        matrix.reverse()
