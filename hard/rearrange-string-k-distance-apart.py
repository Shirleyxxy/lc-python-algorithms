## Time Complexity: O(NlogN)
## Space Complexity: O(N)

from heapq import *
from collections import deque

class Solution:
    def rearrangeString(self, s, k):
        '''
        :type s: str
        :type k: int
        :rtype: str
        '''
        if k <= 1: return s

        char_freq = {}
        for ch in s:
            char_freq[ch] = char_freq.get(ch, 0) + 1

        max_heap = []
        for ch, freq in char_freq.items():
            heappush(max_heap, (-freq, ch))

        res_s, queue = [], deque()
        while max_heap:
            freq, ch = heappop(max_heap)
            res_s.append(ch)
            queue.append((freq+1, ch))

            if len(queue) == k:
                freq, ch = queue.popleft()
                if -freq > 0:
                    heappush(max_heap, (freq, ch))

        return ''.join(res_s) if len(res_s) == len(s) else ''
