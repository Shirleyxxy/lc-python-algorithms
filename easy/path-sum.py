## Time Complexity: O(N)
## Space Complexity: O(H) where H is the tree height
## O(N) in the worst case; O(logN) in the best case 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, sum):
        '''
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        '''
        if not root: return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
