## Time Complexity: O(N)
## Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root: return 0

        queue = deque()
        queue.append(root)
        max_depth = 0
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
