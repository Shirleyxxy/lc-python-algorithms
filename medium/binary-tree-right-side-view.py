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
    def rightSideView(self, root):
        '''
        :type root: TreeNode
        :rtype: List[int]
        '''
        result = []
        if not root: return result

        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr_node = queue.popleft()
                if i == level_size - 1:
                    result.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return result
