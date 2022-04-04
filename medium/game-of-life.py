## Solution 1: O(M * N) space, copy the original board
## We look at the neighbors of a cell in the unmodified copy of the board and change the original board.
## Time complexity: O(M * N)
## Space complexity: O(M * N)


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows, ncols = len(board), len(board[0])
        copy_board = [[board[row][col] for col in range(ncols)] for row in range(nrows)]
        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # iterate through board cell by cell
        for row in range(nrows):
            for col in range(ncols):
                live_neighbors = 0
                for neighbor in neighbors:
                    x, y = row + neighbor[0], col + neighbor[1]
                    # check the validity of the neighboring cell and if it was originally a live cell
                    if 0 <= x < nrows and 0 <= y < ncols and copy_board[x][y] == 1:
                        live_neighbors += 1
                if copy_board[row][col] == 1 and (
                    live_neighbors < 2 or live_neighbors > 3
                ):
                    board[row][col] = 0
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


## Solution 2: O(1) space

## Time complexity: O(M * N)
## Space complexity: O(1)


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 - dead,
        1 - live,
        2 - live --> dead (1 --> 0),
        3 - dead --> live (0 --> 1).
        """
        nrows, ncols = len(board), len(board[0])
        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # iterate through board cell by cell
        for row in range(nrows):
            for col in range(ncols):
                live_neighbors = 0
                for neighbor in neighbors:
                    x, y = row + neighbor[0], col + neighbor[1]
                    # check the validity of the neighboring cell and if it was originally a live cell
                    if (
                        0 <= x < nrows
                        and 0 <= y < ncols
                        and (board[x][y] == 1 or board[x][y] == 2)
                    ):
                        live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 2
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 3

        # get the final representation for the newly updated cell
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == 2:
                    board[row][col] = 0
                if board[row][col] == 3:
                    board[row][col] = 1


## O(1) space solution (slightly better?)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 - dead,
        1 - live,
        2 - dead --> live (0 --> 1),
        3 - live --> dead (1 --> 0).
        """
        nrows, ncols = len(board), len(board[0])
        for row in range(nrows):
            for col in range(ncols):
                live_neighbors = self.countNeighbors(board, row, col)
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 3

        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0

    def countNeighbors(self, board, r, c):
        live_neighbors = 0
        for i in (r - 1, r, r + 1):
            for j in (c - 1, c, c + 1):
                if 0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1:
                    live_neighbors += board[i][j] % 2
        return live_neighbors - board[r][c]
