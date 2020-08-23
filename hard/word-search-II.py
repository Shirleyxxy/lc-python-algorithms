## Time Complexity: O(M * (4 * 3^(L-1)))
## M is the number of cells on the board; L is the maximum length of word
## For backtracking function, initially we have at most 4 directions to explore,
## but further the choices are reduced to at most 3 since we won't go back to where we come from.
## We would traverse at most 4 * 3^(L-1) cells during the backtracking exploration.

## Space Complexity: O(N) - N is the total number of letters in the dictionary
## In the worst case where there is no overlapping of prefixes among the words,
## the Trie would have as many nodes as the letters of all words.

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False


class Trie:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.root = TrieNode()

    def insert(self, word):
        '''
        Inserts a word into the trie.
        :type word: str
        Time Complexity: O(N), N is the length of the word
        Space Complexity: O(N)
        '''
        curr = self.root
        for ch in word:
            # will initialize default TrieNode along the way
            curr = curr.children[ch]
        curr.is_end = True


class Solution:
    def findWords(self, board, words):
        '''
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        '''
        res = []
        # initialize a trie
        trie = Trie()
        root = trie.root
        # insert all the words into trie
        for word in words:
            trie.insert(word)
        # start searching for words
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, '', res)
        return res


    def dfs(self, board, i, j, node, curr_word, res):
        # find a matching word
        if node.is_end:
            res.append(curr_word)
            # avoid duplicates; cases like 'aaa' and 'aaab'
            node.is_end = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        curr_ch = board[i][j]
        node = node.children.get(curr_ch)
        # not in the board
        if not node: return
        # mark as visited
        board[i][j] = '#'
        # explore the four possible directions after matching a character
        self.dfs(board, i-1, j, node, curr_word+curr_ch, res)
        self.dfs(board, i+1, j, node, curr_word+curr_ch, res)
        self.dfs(board, i, j-1, node, curr_word+curr_ch, res)
        self.dfs(board, i, j+1, node, curr_word+curr_ch, res)
        # backtracking
        board[i][j] = curr_ch
