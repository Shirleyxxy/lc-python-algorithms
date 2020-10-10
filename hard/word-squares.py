## Backtracking: "construct all possible combinations of word squares".
## Time Complexity: O(N * 26^L) - N is the number of input words
## L is the length of a single word (this is an upper bound)
## Space Complexity: O(N * L)

class Solution:
    def wordSquares(self, words):
        '''
        :type words: List[str]
        :rtype: List[List[str]]
        '''
        self.words = words
        self.N = len(words[0])
        self.buildPrefixDictionary(self.words)

        res, word_squares = [], []
        for word in words:
            # try with every word as the starting word
            word_squares = [word]
            self.backtracking(1, word_squares, res)
        return res


    def buildPrefixDictionary(self, words):
        self.prefixDictionary = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefixDictionary.setdefault(prefix, set()).add(word)


    def getWordsWithPrefix(self, prefix):
        if prefix in self.prefixDictionary:
            return self.prefixDictionary[prefix]
        else:
            return set([])


    def backtracking(self, step, word_squares, res):
        if step == self.N:
            res.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        # find out all words that start with the given prefix
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, res)
            word_squares.pop()
