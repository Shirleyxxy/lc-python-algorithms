# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## time complexity: O(N)
## space complexity: O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []

        queue = collections.deque([root])
        while queue:
            curr_level, level_size = [], len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr_level)

        return res
