# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Recursive
## Time Complexity: O(H) since one goes from root down to a leaf
## Space Complexity: O(1)
class Solution:
    def closestValue(self, root, target):
        '''
        :type root: TreeNode
        :type target: float
        :rtype: int
        '''
        self.closest = float('inf')
        self.dfs(root, target)
        return self.closest

    def dfs(self, node, target):
        if not node:
            return
        if abs(node.val - target) < abs(self.closest - target):
            self.closest = node.val
        if node.val > target:
            self.dfs(node.left, target)
        else:
            self.dfs(node.right, target)



## Iterative
## Time Complexity: O(H) since one goes from root down to a leaf
## Space Complexity: O(1)
class Solution:
    def closestValue(self, root, target):
        '''
        :type root: TreeNode
        :type target: float
        :rtype: int
        '''
        curr = root
        closest = curr.val
        while curr:
            if abs(curr.val - target) < abs(closest - target):
                closest = curr.val
            if curr.val > target:
                curr = curr.left
            else:
                curr = curr.right
        return closest
