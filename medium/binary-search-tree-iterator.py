## The inorder traversal of a BST gives us the elements in a sorted order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Solution 1: Recursion
## Time Complexity: O(N) is the time taken by the constructor for the iterator.
## O(1) for next(); O(1) for hasNext()
## Space Complexity: O(N) for the array containing all the nodes of BST.
## O(logN) on average for the recursion stack.

class BSTIterator:
    def __init__(self, root):
        '''
        :type root: TreeNode
        '''
        # array containing all the nodes in the sorted order
        self.nodes = []
        # pointer to the next smallest element in the BST
        self.index = -1
        self._inorder(root)

    def _inorder(self, node):
        if not node: return
        self._inorder(node.left)
        self.nodes.append(node.val)
        self._inorder(node.right)

    def next(self):
        '''
        Return the next smallest number
        :rtype: int
        '''
        if self.hasNext():
            self.index += 1
            return self.nodes[self.index]

    def hasNext(self):
        '''
        Return whether we have a next smallest number
        :rtype: bool
        '''
        return self.index+1 < len(self.nodes)


## Solution 2: Stack (Iterative approach)
## Key idea: for a given node, the next smallest element will always be the leftmost
## element in its tree.
## Time Complexity: O(1) for hasNext(); O(1) amortized for next()
## Each node gets pushed and popped exactly once in next() when iterating over N nodes.
## 2N * O(1) over N calls to next(), making it O(1) on average, or O(1) amortized.
## Space Complexity: O(logN) on average for the recursion stack

class BSTIterator:
    def __init__(self, root):
        '''
        :type root: TreeNode
        '''
        self.stack = []
        self._inorder_left(root)

    def _inorder_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        '''
        Return the next smallest number
        :rtype: int
        '''
        if self.hasNext():
            top_node = self.stack.pop()
            if top_node.right:
                self._inorder_left(top_node.right)
            return top_node.val

    def hasNext(self):
        '''
        Return whether we have a next smallest number
        :rtype: bool
        '''
        return len(self.stack) > 0
