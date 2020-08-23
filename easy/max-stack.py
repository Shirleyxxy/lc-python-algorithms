## Time Complexity: O(n) for the popMax operation, and O(1) for the other operations.
## Space Complexity: O(n), the maximum size of the stack.

## Solution 1: one stack
class MaxStack:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.stack = []


    def push(self, x):
        '''
        Push element x onto stack.
        :type x: int
        :rtype: None
        '''
        if self.stack == []:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.stack[-1][1])))


    def pop(self):
        '''
        Remove the element on top of the stack and return it.
        :rtype: int
        '''
        if self.stack != []:
            top_elem = self.stack[-1][0]
            self.stack.pop()
            return top_elem


    def top(self):
        '''
        Get the element on the top.
        :rtype: int
        '''
        if self.stack != []:
            return self.stack[-1][0]


    def peekMax(self):
        '''
        Retrieve the maximum element in the stack.
        :rtype: int
        '''
        if self.stack != []:
            return self.stack[-1][1]


    def popMax(self):
        '''
        Retrieve the maximum element in the stack, and remove it.
        If you find more than one maximum elements, only remove the top most one.
        :rtype: int
        '''
        max_elem = self.peekMax()
        buff = []
        while self.top() != max_elem:
            buff.append(self.pop())
        self.pop()
        while buff != []:
            self.push(buff.pop())
        return max_elem


## Solution 2: two stacks
class MaxStack:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.stack = []
        self.max_stack = []


    def push(self, x):
        '''
        Push element x onto stack.
        :type x: int
        :rtype: None
        '''
        self.stack.append(x)
        if self.max_stack == []:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))


    def pop(self):
        '''
        Remove the element on top of the stack and return it.
        :rtype: int
        '''
        if self.stack != []:
            self.max_stack.pop()
            return self.stack.pop()


    def top(self):
        '''
        Get the element on the top.
        :rtype: int
        '''
        if self.stack != []:
            return self.stack[-1]


    def peekMax(self):
        '''
        Retrieve the maximum element in the stack.
        :rtype: int
        '''
        if self.max_stack != []:
            return self.max_stack[-1]


    def popMax(self):
        '''
        Retrieve the maximum element in the stack, and remove it.
        If you find more than one maximum elements, only remove the top most one.
        :rtype: int
        '''
        if self.max_stack != []:
            max_elem = self.max_stack[-1]
            buff = []
            while self.top() != max_elem:
                buff.append(self.pop())
            self.pop()
            while buff != []:
                self.push(buff.pop())
            return max_elem
