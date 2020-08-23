## Breadth First Search: find the shortest path from a start node to a destination node.
## Time Complexity: O(M^2 * N)
## Space Complexity: O(M^2 * N)
## M is the length of each word
## N is the total number of words in the input word list 

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        '''
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        '''
        # Pre-processing the words in the wordList to efficiently find the neighboring nodes
        # for any given word
        # Replace the letter of a word by a non-alphabet _
        # Key is the generic word with _ and value is a list of words which have the same intermediate
        # generic word
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                generic_word = word[:i] + '_' + word[i+1:]
                d[generic_word].append(word)

        queue, visited = deque([(beginWord, 1)]), set()
        while queue:
            curr_word, level = queue.popleft()
            if curr_word not in visited:
                # mark visited
                visited.add(curr_word)
                # check the termination condition
                if curr_word == endWord:
                    return level
                # add the neighbors of the current word to the queue
                for i in range(len(curr_word)):
                    generic_word = curr_word[:i] + '_' + curr_word[i+1:]
                    neighbor_words = d[generic_word]
                    for neighbor in neighbor_words:
                        if neighbor not in visited:
                            queue.append((neighbor, level+1))
        # no transformation sequence
        return 0
