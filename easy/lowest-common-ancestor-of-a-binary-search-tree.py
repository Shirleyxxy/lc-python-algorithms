# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## Recursive solution
## Time Complexity: O(N)
## Space Complexity: O(N)
## The max amount of space utilized by the recursion stack would be N
## since the height of a skewed BST could be N.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # both p and q are in the right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # both p and q are in the left subtree
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # we have found the split point, i.e. the LCA node
        else:
            return root


## Iterative solution
## Time Complexity: O(N) for the worst case; O(logN) for a balanced BST
## Space Complexity: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # found the split point
            else:
                return root
