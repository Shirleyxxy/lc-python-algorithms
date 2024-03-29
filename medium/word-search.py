## DFS + Backtracking
## Time Complexity: O(nrows * ncols * 3^L)
## For backtracking function, initially we have at most 4 directions to explore,
## but further the choices are reduced to at most 3 since we won't go back to
## where we come from.
## Space Complexity: O(L)
## L = len(word)


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, curr_word):
        # find match for each character in the word
        if len(curr_word) == 0:
            return True
        # check the current status
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or board[i][j] != curr_word[0]
        ):
            return False
        # save the character matched for backtracking later
        curr_match = board[i][j]
        # mark it as visited
        board[i][j] = "#"
        # explore the four possible directions
        res = (
            self.dfs(board, i - 1, j, curr_word[1:])
            or self.dfs(board, i + 1, j, curr_word[1:])
            or self.dfs(board, i, j + 1, curr_word[1:])
            or self.dfs(board, i, j - 1, curr_word[1:])
        )
        # backtracking
        board[i][j] = curr_match
        return res


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.search(r, c, 0):
                    return True
        return False

    def search(self, row, col, i):
        if i == len(self.word):
            return True
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return False
        if self.board[row][col] != self.word[i]:
            return False
        matched_ch = self.board[row][col]
        self.board[row][col] = "*"
        res = (
            self.search(row + 1, col, i + 1)
            or self.search(row, col + 1, i + 1)
            or self.search(row - 1, col, i + 1)
            or self.search(row, col - 1, i + 1)
        )
        self.board[row][col] = matched_ch
        return res
