## Time Complexity: O(R * C)^2
## We need O(R * C) to scan through the board to crush and drop for one round.
## We need at most (R * C) / 3 rounds to reach the stable state. ==> O(R * C)^2.
## Space Complexity: O(1) additional complexity, as we edit the board in place.


class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        nrows, ncols = len(board), len(board[0])
        # step 1: we check the state of the board after each round, flagging each candy that should be removed
        # We design the while loop so each time the set is re-initialized; once we reach the stable state (the
        # crush set stays empty), we break out of the loop and return the board in the stable state
        while True:
            crush = set()
            for i in range(nrows):
                for j in range(ncols):
                    # check horizontally in groups of 3
                    if (
                        j > 1
                        and board[i][j] != 0
                        and board[i][j] == board[i][j - 1] == board[i][j - 2]
                    ):
                        crush.update([(i, j), (i, j - 1), (i, j - 2)])
                    # check vertically in groups of 3
                    if (
                        i > 1
                        and board[i][j] != 0
                        and board[i][j] == board[i - 1][j] == board[i - 2][j]
                    ):
                        crush.update([(i, j), (i - 1, j), (i - 2, j)])

            # step 2
            # reach the stable state --> break the loop and return the board
            if len(crush) == 0:
                break
            # crush the flagged candy
            for i, j in crush:
                board[i][j] = 0

            # step 3: drop
            # check column by column
            for j in range(ncols):
                idx = nrows - 1
                # in the reverse order
                for i in range(nrows - 1, -1, -1):
                    # if non-zero element: assign it to the right place
                    if board[i][j] != 0:
                        board[idx][j] = board[i][j]
                        idx -= 1
                # empty the cells above (row 0 through row idx)
                for i in range(idx + 1):
                    board[i][j] = 0

        return board
