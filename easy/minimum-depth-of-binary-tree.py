# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Solution 1 - Recursion
## Time Complexity: O(N)
## Space Complexity: O(N) in the worst case; O(logN) in the best case
class Solution:
    def minDepth(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root: return 0
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


## Solution 2 - Iteration
## Time Complexity: O(N)
## Space Complexity: O(N)
from collections import deque
class Solution:
    def minDepth(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root: return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
