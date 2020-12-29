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


## Solution 1
## Store the sum at each level without any weights.
## After traversing the nested list, we will get the maximum level and a dictionary
## storing the sum for each level. Then we can calculate the weighted sum.
## Time Complexity: O(N)
## Space Complexity: O(D)
from collections import defaultdict

class Solution:
    def depthSumInverse(self, nestedList):
        '''
        :type nestedList: List[NestedInteger]
        :rtype: int
        '''
        self.cache = defaultdict(int)
        self.max_level = -1
        self.traverse(nestedList, 1)
        res = 0
        for level, _sum in self.cache.items():
            res += _sum * (self.max_level - level + 1)
        return res


    def traverse(self, nestedList, level):
        self.max_level = max(self.max_level, level)
        for el in nestedList:
            if el.isInteger():
                self.cache[level] += el.getInteger()
            else:
                self.traverse(el.getList(), level+1)
        return


## Solution 2
## Instead of multiplying by depth, add integers multiple times (by going level by level and adding the unweighted
## sum to the weighted sum after each level).
## Time Complexity: O(N^2)
class Solution:
    def depthSumInverse(self, nestedList):
        '''
        :type nestedList: List[NestedInteger]
        :rtype: int
        '''
        res, level_sum = 0, 0
        while nestedList:
            next_level_list = []
            for el in nestedList:
                if el.isInteger():
                    level_sum += el.getInteger()
                else:
                    for val in el.getList():
                        next_level_list.append(val)
            res += level_sum
            nestedList = next_level_list
        return res
