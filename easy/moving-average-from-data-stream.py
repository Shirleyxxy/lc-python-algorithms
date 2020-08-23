## queue.Queue
from queue import Queue

class MovingAverage:
    def __init__(self, size):
        '''
        Initialize your data structure here.
        :type size: int
        '''
        self.queue = Queue(maxsize = size)
        self.cur_sum = 0


    def next(self, val):
        '''
        Calculate the moving average.
        :type val: int
        :rtype: float
        '''
        if self.queue.full():
            self.cur_sum -= self.queue.get()
        self.queue.put(val)
        self.cur_sum += val
        return float(self.cur_sum) / self.queue.qsize()


## collections.deque
## Time Complexity: O(1)
## Space Complexity: O(N) - N is the size of the moving window

from collections import deque

class MovingAverage:
    def __init__(self, size):
        '''
        Initialize your data structure here.
        :type size: int
        '''
        self.queue = deque()
        self.size = size
        self.window_sum = 0
        self.count = 0

    def next(self, val):
        '''
        Calculate the moving average.
        :type val: int
        :rtype: float
        '''
        if self.count < self.size:
            self.queue.append(val)
            self.window_sum += val
            self.count += 1
        else:
            self.window_sum -= self.queue.popleft()
            self.queue.append(val)
            self.window_sum += val
        return float(self.window_sum) / self.count
