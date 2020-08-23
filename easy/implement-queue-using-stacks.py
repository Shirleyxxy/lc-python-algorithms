## Time Complexity: push - O(1), pop - amortized O(1), worst-case O(N), empty - O(1), peek - amortized O(1), worst-case O(N)
## Space Complexity: O(N) to store the elements

class MyQueue:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.in_stack, self.out_stack = [], []


    def push(self, x):
        '''
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        '''
        self.in_stack.append(x)


    def pop(self):
        '''
        Removes the element from the front of queue and returns that element.
        :rtype: int
        '''
        self.move()
        return self.out_stack.pop()


    def peek(self):
        '''
        Get the front element.
        :rtype: int
        '''
        self.move()
        return self.out_stack[-1]


    def empty(self):
        '''
        Returns whether the queue is empty.
        :rtype: boolean
        '''
        return (not self.in_stack) and (not self.out_stack)


    def move(self):
        '''
        Moves the elements from in_stack to out_stack so the order can be reversed.
        :rtype: None.
        '''
        # when self.out_stack is empty, there is a need for data transfer
        # between self.in_stack and self.out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
