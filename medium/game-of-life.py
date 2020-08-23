## Have a copy of the board; we look at the neighbors of a cell
## in the unmodified copy of the board and change the original board.
## Time Complexity: O(M * N), M = nrows, N = ncols
## Space Complexity: O(M * N)

class Solution:
    def gameOfLife(self, board):
        '''
        :type board: List[List[int]]
        Dead:0; live: 1
        Do not return anything, modify board in-place instead.
        '''
        nrows, ncols = len(board), len(board[0])
        # create a copy of the original board
        board_copy = [[board[row][col] for col in range(ncols)] for row in range(nrows)]
        neighbors = [(1,0), (-1,0), (-1,-1), (-1,1), (0,-1), (0,1), (1,-1), (1,1)]

        for row in range(nrows):
            for col in range(ncols):
                # for each cell we count the number of live neighbors
                live_neighbors = 0
                for neighbor in neighbors:
                    x, y = row + neighbor[0], col + neighbor[1]
                    # note the validity of the neighboring cells
                    if 0 <= x < nrows and 0 <= y < ncols and board_copy[x][y] == 1: live_neighbors += 1
                # rule 1 or rule 3
                if board_copy[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # rule 4
                if board_copy[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


## How to solve it in-place?
## Time Complexity: O(M * N), M = nrows, N = ncols
## Space Complexity: O(1)

class Solution:
    def gameOfLife(self, board):
        '''
        :type board: List[List[int]]
        Dead:0; live: 1
        Do not return anything, modify board in-place instead.
        '''
        nrows, ncols = len(board), len(board[0])
        neighbors = [(1,0), (-1,0), (-1,-1), (-1,1), (0,-1), (0,1), (1,-1), (1,1)]

        for row in range(nrows):
            for col in range(ncols):
                live_neighbors = 0
                for neighbor in neighbors:
                    x, y = row + neighbor[0], col + neighbor[1]
                    if 0 <= x < nrows and 0 <= y < ncols and abs(board[x][y]) == 1: live_neighbors += 1
                ## live --> dead: -1; dead --> live: 2
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
        # iterate through the board once more
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
