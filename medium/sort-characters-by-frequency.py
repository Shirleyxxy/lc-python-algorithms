## Time Complexity: O(N*logN)
## Space Complexity: O(N)

from heapq import *

class Solution:
    def frequencySort(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        char_freq = {}
        for ch in s:
            char_freq[ch] = char_freq.get(ch, 0) + 1

        max_heap = []
        for ch, freq in char_freq.items():
            heappush(max_heap, (-freq, ch))

        res_s = ''
        while max_heap:
            freq, ch = heappop(max_heap)
            res_s += ch * (-freq)
        return res_s
