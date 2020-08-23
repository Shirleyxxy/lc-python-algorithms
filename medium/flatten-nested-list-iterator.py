# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer.
#        Return None if this NestedInteger holds a nested list.
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list.
#        Return None if this NestedInteger holds a single integer.
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class NestedIterator(object):
    def __init__(self, nestedList):
        '''
        Push all elements in nestedList onto stack in reverse order.
        :type nestedList: nestedInteger
        '''
        self.stack = nestedList[::-1]


    def next(self):
        '''
        If the stack still contains items, then it is guaranteed the top is an integer.
        This integer is popped and returned.
        :rtype: int
        '''
        return self.stack.pop().getInteger()


    def hasNext(self):
        '''
        Returns true if the stack still contains items, false if not.
        :rtype: bool
        '''
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # flatten to make sure the top of the stack is an integer
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


## Solution 2: Define a flatten function using stack

class NestedIterator(object):
    def __init__(self, nestedList):
        '''
        Push all elements in nestedList onto stack in reverse order.
        :type nestedList: nestedInteger
        '''
        self.stack = nestedList[::-1]


    def flatten(self):
        '''
        Check if the top of the stack is still a list.
        If it is a list, push the contents of the list onto stack in reverse order.
        '''
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(self.stack.pop().getList()[::-1])


    def next(self):
        '''
        If the stack still contains items, then it is guaranteed the top is an integer.
        This integer is popped and returned.
        :rtype: int
        '''
        return self.stack.pop().getInteger()


    def hasNext(self):
        '''
        Returns true if the stack still contains items, false if not.
        :rtype: bool
        '''
        self.flatten()
        return len(self.stack) > 0
