## Time Complexity: O(NlogK)
## Space Complexity: O(N)


from heapq import *

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words, k):
        '''
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        '''
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        min_heap = []
        for word, freq in word_freq.items():
            heappush(min_heap, Word(freq, word))
            if len(min_heap) > k:
                heappop(min_heap)

        res = []
        while min_heap:
            res.append(heappop(min_heap).word)
        return res[::-1]
