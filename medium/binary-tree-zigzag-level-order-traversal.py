## Time Complexity: O(N)
## Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        '''
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        result = []
        if not root: return result

        queue = collections.deque([root])
        left_to_right = True
        while queue:
            curr_level, level_size = deque(), len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                if left_to_right:
                    curr_level.append(curr_node.val)
                else:
                    curr_level.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            result.append(curr_level)
            left_to_right = not left_to_right
        return result
