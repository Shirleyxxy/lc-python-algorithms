# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


## BFS
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def depthSum(self, nestedList):
        '''
        :type nestedList: List[NestedInteger]
        :rtype: int
        '''
        depth, res = 1, 0
        while nestedList:
            res += depth * sum([el.getInteger() for el in nestedList if el.isInteger()])
            # concatenate the lists to process for the next iteration
            nestedList = sum([el.getList() for el in nestedList if not el.isInteger()], [])
            depth += 1
        return res


## DFS
## Time Complexity: O(N) - total number of nested elements
## Space Complexity: O(D) - depth of the nested list
class Solution:
    def depthSum(self, nestedList):
        '''
        :type nestedList: List[NestedInteger]
        :rtype: int
        '''
        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, depth):
        res = 0
        for el in nestedList:
            if el.isInteger():
                res += el.getInteger() * depth
            else:
                res += self.dfs(el.getList(), depth + 1)
        return res
