## Solution 1 - Readable, easy to follow the logic
## Iterate three times over the board to check rows, columns, and sub-boxes.
## Due to the fixed size of the board (9*9), both time & space complexity can be
## considered as O(1).
## For n*n board, the time & space complexity are O(N^2).

class Solution:
    def isValidSudoku(self, board):
        '''
        :type board: List[List[str]]
        :rtype: bool
        '''
        def is_valid(unit):
            vals = [val for val in unit if val != '.']
            return len(vals) == len(set(vals))

        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True

        def is_valid_col(board):
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True

        def is_valid_square(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                    if not is_valid(square):
                        return False
            return True

        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)


## Solution 2 - One iteration
## Same Time & Space Complexity
class Solution:
    def isValidSudoku(self, board):
        '''
        :type board: List[List[str]]
        :rtype: bool
        '''
        vals = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != '.':
                    # (i//3, j//3) identifies one of the 9 3x3 sub-boxes
                    # use of (val, j) not (j, val) to distinguish between rows and columns
                    # e.g. ('4', 4) and (4, '4')
                    vals += [(i, val), (val, j), (i//3, j//3, val)]
        return len(vals) == len(set(vals))
