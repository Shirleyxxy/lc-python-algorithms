## Time Complexity: O(logN) for push and pop
## Space Complexity: O(N)

from heapq import *

class Element:
    def __init__(self, val, freq, seq):
        self.val = val
        self.freq = freq
        self.seq = seq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        else:
            return self.seq > other.seq


class FreqStack:
    def __init__(self):
        self.seq = 0
        self.max_heap = []
        self.freq_map = {}

    def push(self, x):
        '''
        :type x: int
        '''
        self.freq_map[x] = self.freq_map.get(x, 0) + 1
        heappush(self.max_heap, Element(x, self.freq_map[x], self.seq))
        self.seq += 1

    def pop(self):
        '''
        :rtype: int
        '''
        num = heappop(self.max_heap).val
        if self.freq_map[num] > 1:
            self.freq_map[num] -= 1
        else:
            del self.freq_map[num]
        return num


## Optimized version
## Time Complexity: O(1) for push and pop
## Space Complexity: O(N)

class FreqStack:
    def __init__(self):
        # frequency of an element
        self.freq = collections.Counter()
        # mapping from frequency to a stack of elements with that frequency
        self.group = collections.defaultdict(list)
        # current maximum frequency of any element in the stack
        self.max_freq = 0

    def push(self, x):
        self.freq[x] += 1
        self.max_freq = max(self.max_freq, self.freq[x])
        self.group[self.freq[x]].append(x)

    def pop(self):
        num = self.group[self.max_freq].pop()
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        self.freq[num] -= 1
        return num
