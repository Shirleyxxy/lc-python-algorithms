# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        '''
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        '''
        if not root:
            return None
        if root.val == val:
            return root
        # search the left subtree
        elif root.val > val:
            return self.searchBST(root.left, val)
        # search the right subtree
        else:
            return self.searchBST(root.right, val)
