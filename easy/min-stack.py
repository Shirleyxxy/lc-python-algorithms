## Time Complexity: O(1) for all operations
## Space Complexity: O(N)

## Solution 1: One stack
class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        Remove the element on top of the stack.
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]


## Solution 2: Two stacks
class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # a standard stack keeping track of the order numbers arrived
        self.stack = []
        # keeps track of the current minimum
        self.min_stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        """
        Remove the element on top of the stack.
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
