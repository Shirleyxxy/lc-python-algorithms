## Similar problem: lc269 - alien dictionary
## Time Complexity: O(M * N)
## Space Complexity: O(1)

class Solution:
    def isAlienSorted(self, words, order):
        '''
        :type words: List[str]
        :type order: str
        :rtype: bool
        '''
        # create an order dictionary
        mapping = {c:i for i, c in enumerate(order)}
        # look into each pair of adjacent words
        for w1, w2 in zip(words, words[1:]):
            # latter word is a substring of the former word
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for c1, c2 in zip(w1, w2):
                # stop the comparison if the current letter of the former word is in lower order
                # continue to check the next two adjacent words
                if mapping[c1] < mapping[c2]:
                    break
                # return False if any letter of the former word is in higher order
                elif mapping[c1] > mapping[c2]:
                    return False
                else:
                    continue
        return True
