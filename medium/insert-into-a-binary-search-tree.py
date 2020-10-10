## It is guaranteed that the new value does not exist in the original BST.
## Idea: one could always insert new node as a child of the leaf.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Recursive
## Time: O(H) - O(logN) on average, O(N) in the worst case
## Space: O(H) - recursion stack
class Solution:
    def insertIntoBST(self, root, val):
        '''
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        '''
        if not root:
            return TreeNode(val)
        # insert into the left subtree
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        # insert into the right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


## Iterative
## Time: O(H) - O(logN) on average, O(N) in the worst case
## Space: O(1)
class Solution:
    def insertIntoBST(self, root, val):
        '''
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        '''
        if not root: return TreeNode(val)
        node = root
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root
