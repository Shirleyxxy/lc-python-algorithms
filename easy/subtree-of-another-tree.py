# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Recursion
## Time Complexity: O(|s| * |t|)
## Space Complexity: O(|s|) - the depth of the recursion tree

class Solution:
    def isSubtree(self, s, t):
        '''
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        '''
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        '''
        Check the equality of the two trees.
        '''
        if not (s and t):
            return s is t
        return (s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right))
