# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## Solution 1 - Iterative using stack + inorder traversal
## Idea: Left --> Node --> Right order of inorder traversal means for BST
## that each element should be smaller than the next one.
## Check lc94: Binary tree inorder traversal
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def isValidBST(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        stack, res = [(root, False)], []
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    if res and curr.val <= res[-1]:
                        return False
                    res.append(curr.val)
                else:
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
        return True


## Solution 2 - Stack (lower & upper limits)
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def isValidBST(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        if not root: return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node: continue
            val = node.val
            if val <= lower or val >= upper:
                return False
            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))
        return True


## Solution 3 - Recursion
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def isValidBST(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        return self.isValidBSTFrom(root)

    def isValidBSTFrom(self, node, lo = float('-inf'), hi = float('inf')):
        if not node: return True
        if not lo < node.val < hi:
            return False
        return self.isValidBSTFrom(node.left, lo, node.val) and self.isValidBSTFrom(node.right, node.val, hi)
