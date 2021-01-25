## Bottom-up DP
## Time Complexity: O(N), N = number of cells in the triangle
## Space Complexity: O(1) since we modify the input triangle in-place
class Solution:
    def minimumTotal(self, triangle):
        '''
        :type triangle: List[List[int]]
        :rtype: int
        '''
        # the min pathsums for the cells on the bottom row are the values of the cells themselves
        # we then work from bottom to top
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
