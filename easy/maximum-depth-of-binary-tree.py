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
    def maxDepth(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


## Solution 2 - Iteration
## Time Complexity: O(N)
## Space Complexity: O(N)
from collections import deque
class Solution:
    def maxDepth(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root: return 0
        max_depth = 0
        queue = deque([root])
        while queue:
            max_depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return max_depth
