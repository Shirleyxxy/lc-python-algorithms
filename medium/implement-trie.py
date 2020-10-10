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
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True


    def search(self, word):
        '''
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        curr = self.root
        for ch in word:
            curr = curr.children.get(ch)
            if not curr:
                return False
        return curr.is_end


    def startsWith(self, prefix):
        '''
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        curr = self.root
        for ch in prefix:
            curr = curr.children.get(ch)
            if not curr:
                return False
        return True
