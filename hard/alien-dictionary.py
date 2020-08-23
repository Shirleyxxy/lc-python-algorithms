## Similar:
## Check Bloomberg-phone.py
## Check lc953 - Verifying an alien dictionary
##################
## Topological sort + BFS
## Time Complexity: O(V + E), V is the total number of different characters
## E is the total number of rules in the alien language
## Since, at most, each pair of words can give us one rule, therefore,
## we can conclude that the upper bound for the rules is O(N) where ‘N’ is
## the number of words in the input.
## So, we can say that the time complexity of our algorithm is O(V + N).

## Space Complexity: O(V + N)

from collections import deque

class Solution:
    def alienOrder(self, words):
        '''
        :type words: List[str]
        :rtype: str
        '''
        if len(words) == 0: return ''

        in_degrees = {}
        graph = {}
        for word in words:
            for ch in word:
                in_degrees[ch] = 0
                graph[ch] = []
        # look into each pair of adjacent words
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                        in_degrees[c2] += 1
                    # only the first different character between the two words will
                    # help us find the order
                    break
            # The else block just after for/while is executed only when
            # the loop is NOT terminated by a break statement
            else:
                # if the second word is a substring of the first word
                # the order is invalid
                if len(w1) > len(w2): return ''

        # find all the sources for BFS
        sources = deque([ch for ch in in_degrees if in_degrees[ch] == 0])
        sorted_order = []

        while sources:
            ch = sources.popleft()
            sorted_order.append(ch)
            for child in graph[ch]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        # if not all letters are in the output, that means there was a cycle and so no valid ordering
        if len(sorted_order) != len(in_degrees):
            return ''
        return ''.join(sorted_order)        
