## DFS
## Continue the DFS if
## 1. The next cell is within bounds.
## 2. The next cell has the same color as the source cell.

## Time Complexity: O(N), N is the number of pixels (cells) in the image.
## Space Complexity: O(N) for the call stack
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        '''
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :newColor: int
        :rtype: List[List[int]]
        '''
        nrows, ncols, orig_color = len(image), len(image[0]), image[sr][sc]

        def dfs(row, col):
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                return
            if image[row][col] != orig_color:
                return
            image[row][col] = newColor
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        # if the new color is the same as the original color
        # there will be an infinite loop
        if orig_color != newColor:
            dfs(sr, sc)

        return image


## BFS
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        '''
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :newColor: int
        :rtype: List[List[int]]
        '''
        nrows, ncols, orig_color = len(image), len(image[0]), image[sr][sc]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # avoid the infinite loop
        if orig_color != newColor:
            queue = collections.deque([(sr, sc)])
            while queue:
                row, col = queue.popleft()
                image[row][col] = newColor
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if 0 <= new_row < nrows and 0 <= new_col < ncols and image[new_row][new_col] == orig_color:
                        queue.append((new_row, new_col))
        return image
