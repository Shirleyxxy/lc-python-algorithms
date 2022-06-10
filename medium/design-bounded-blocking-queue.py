import threading

## Condition Objects
## Ref: https://docs.python.org/3/library/threading.html#condition-objects

## A condition variable obeys the context management protocol:
## using the with statement acquires the associated lock for the duration of the enclosed block.

## The idea is to orchestrate the synchronity of the producers and consumers.
## When the bounded blocking queue is full, all producers trying to enqueue will be blocked
## calling self.cond.wait() until at least one consumer deques. Similarly, all consumers
## trying to deque while the queue is empty will be blocked calling self.cond.wait() until
## at least one producer enqueues.


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = collections.deque()
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.cond:
            while len(self.queue) >= self.capacity:
                # releases the lock, and then blocks until another thread awakens it
                # by calling notify()
                self.cond.wait()
            self.queue.append(element)
            self.cond.notify()

    def dequeue(self) -> int:
        with self.cond:
            while len(self.queue) == 0:
                self.cond.wait()
            res = self.queue.popleft()
            self.cond.notify()
        return res

    def size(self) -> int:
        with self.cond:
            return len(self.queue)
