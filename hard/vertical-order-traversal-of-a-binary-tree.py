# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## time complexity: O(N * log(N/K)), N = number of nodes, K = number of columns in the tree
## space complexity: O(N)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])  # node, col, depth
        min_col = max_col = 0

        while queue:
            node, col, depth = queue.popleft()
            cols[col].append((depth, node.val))
            if node.left:
                queue.append((node.left, col - 1, depth + 1))
                min_col = min(min_col, col - 1)
            if node.right:
                queue.append((node.right, col + 1, depth + 1))
                max_col = max(max_col, col + 1)

        res = []
        # from left to right
        for i in range(min_col, max_col + 1):
            # from top to bottom
            # if two nodes have the same position, get the smaller value first
            # sort by depth first, then value in ascending order
            col = [val[1] for val in sorted(cols[i])]
            res.append(col)

        return res
