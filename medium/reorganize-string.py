## Time Complexity: O(NlogN)
## Space Complexity: O(N)

from heapq import *

class Solution:
    def reorganizeString(self, S):
        '''
        :type S: str
        :rtype: str
        '''
        char_freq = {}
        for ch in S:
            char_freq[ch] = char_freq.get(ch, 0) + 1

        max_heap = []
        for ch, freq in char_freq.items():
            heappush(max_heap, (-freq, ch))

        res_s = []
        prev_ch, prev_freq = None, 0
        while max_heap:
            freq, ch = heappop(max_heap)
            res_s.append(ch)
            # add the previous entry back in the heap if its frequency is greater than 0
            if prev_ch and -prev_freq > 0:
                heappush(max_heap, (prev_freq, prev_ch))
            prev_ch = ch
            prev_freq = freq + 1

        return ''.join(res_s) if len(res_s) == len(S) else ''
