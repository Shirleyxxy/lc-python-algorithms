## A height-balanced binary tree is defined as:
## A binary tree in which the left and right subtrees of every node
## differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Solution 1 - 1. Check if the difference between the heights of the two subtrees are not bigger than 1
## 2. Check if both the left subtree and the right subtree are also balanced
## Time Complexity: O(NlogN)
## Space Complexity: O(N)
class Solution:
    def isBalanced(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        if not root: return True
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        return abs(left_h - right_h) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node: return 0
        return 1 + max(self.height(node.left), self.height(node.right))


## Solution 2
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def isBalanced(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        return self.DFSHeight(root) != -1

    def DFSHeight(self, node):
        if not node: return 0
        left = self.DFSHeight(node.left)
        right = self.DFSHeight(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)
