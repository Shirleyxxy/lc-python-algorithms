## My solution - Dictionary
## Time: O(1) for lookup & update
## Space: O(M) where M is the size of all incoming messages
## Problem with this solution: the usage of memory would keep on growing over the time
## The dictionary would have an entry for each unique message that has appeared

from collections import defaultdict

class Logger:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        # {key:value} = {message:latest timestamp}
        self.logger = defaultdict(lambda: -1)


    def shouldPrintMessage(self, timestamp, message):
        '''
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.

        :type timestamp: int
        :type message: str
        :rtype: bool
        '''
        if self.logger[message] == -1 or timestamp - self.logger[message] >= 10:
            self.logger[message] = timestamp
            return True
        else:
            return False


## Solution 2 - Queue + Set
## Time: O(N), where N is the size of the queue
## Space: O(N), where N is the size of the queue
from collections import deque

class Logger:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self._msg_set = set()
        self._msg_queue = deque()


    def shouldPrintMessage(self, timestamp, message):
        '''
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.

        :type timestamp: int
        :type message: str
        :rtype: bool
        '''
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break

        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
