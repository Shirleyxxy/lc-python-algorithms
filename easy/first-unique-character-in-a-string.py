## My Solution: Dictionary + Min heap
## Time Complexity: O(N*logN)
## Space Complexity: O(N)

from heapq import *

class Solution:
    def firstUniqChar(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        char_freq = {}
        for ch in s:
            char_freq[ch] = char_freq.get(ch, 0) + 1

        min_heap = []
        for i, ch in enumerate(s):
            if char_freq[ch] == 1:
                heappush(min_heap, (i, ch))

        return min_heap[0][0] if min_heap else -1


## Optimized Solution: Dictionary + Set
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def firstUniqChar(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        d, seen = {}, set()
        for idx, ch in enumerate(s):
            if ch not in seen:
                d[ch] = idx
                seen.add(ch)
            elif ch in d:
                del d[ch]
        return min(d.values()) if d else -1


## Time Complexity: O(N)
## Space Complexity: can be considered as O(1) since English alphabet contains 26 letters
## Best solution: Use Counter / create a dictionary, then iterate through the string from left to right.
class Solution:
    def firstUniqChar(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        freq = collections.Counter(s)
        for idx, ch in enumerate(s):
            if freq[ch] == 1:
                return idx
        return -1


class Solution:
    def firstUniqChar(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
