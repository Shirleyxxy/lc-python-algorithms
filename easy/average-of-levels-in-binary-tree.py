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
    def averageOfLevels(self, root):
        '''
        :type root: TreeNode
        :rtype: List[float]
        '''
        result = []
        if not root: return result

        queue = deque()
        queue.append(root)
        while queue:
            curr_sum, level_size = 0, len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_sum += curr_node.val
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(curr_sum / level_size)
        return result
