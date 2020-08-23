# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        '''
        :type root: TreeNode
        :rtype: List[str]
        '''
        if root is None:
            return []
        path = str(root.val)
        res = []
        self.traverse(root, path, res)
        return res

    def traverse(self, root, path, res):
        if root.left is None and root.right is None:
            res.append(path)
        if root.left is not None:
            self.traverse(root.left, path + '->' + str(root.left.val), res)
        if root.right is not None:
            self.traverse(root.right, path + '->' + str(root.right.val), res)
