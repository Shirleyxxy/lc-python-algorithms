## DFS + Backtracking
## Time Complexity: O(nrows * ncols * 3^L)
## For backtracking function, initially we have at most 4 directions to explore,
## but further the choices are reduced to at most 3 since we won't go back to
## where we come from.
## Space Complexity: O(L)
## L = len(word)

class Solution:
    def exist(self, board, word):
        '''
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        '''
        if not board: return False
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
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != curr_word[0]:
            return False
        # save the character matched for backtracking later
        curr_match = board[i][j]
        # mark it as visited
        board[i][j] = '#'
        # explore the four possible directions
        res = self.dfs(board, i-1, j, curr_word[1:]) or self.dfs(board, i+1, j, curr_word[1:]) \
              or self.dfs(board, i, j+1, curr_word[1:]) or self.dfs(board, i, j-1, curr_word[1:])
        # backtracking
        board[i][j] = curr_match
        return res
