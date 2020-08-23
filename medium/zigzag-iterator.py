## Downcounter + iterator
## Time Complexity: O(1)
## Space Complexity: O(1)

class ZigzagIterator:
    def __init__(self, v1, v2):
        '''
        :type v1: List[int]
        :type v2: List[int]
        '''
        self.queue = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        '''
        :rtype: int
        '''
        len, iter = self.queue.pop(0)
        if len > 1:
            self.queue.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        '''
        :rtype: bool
        '''
        return bool(self.queue)


## Without iterator
## Time Complexity: O(1) for next() and hasNext()
## Space Complexity: O(N) for the vector

class ZigzagIterator:
    def __init__(self, v1, v2):
        '''
        :type v1: List[int]
        :type v2: List[int]
        '''
        self.v = [v1, v2]
        self.queue = collections.deque()
        for i, v in enumerate(self.v):
            if v:
                self.queue.append((i, 0))

    def next(self):
        '''
        :rtype: int
        '''
        v_idx, el_idx = self.queue.popleft()
        val = self.v[v_idx][el_idx]
        if el_idx + 1 < len(self.v[v_idx]):
            self.queue.append((v_idx, el_idx+1))
        return val

    def hasNext(self):
        '''
        :rtype: bool
        '''
        return bool(self.queue)
