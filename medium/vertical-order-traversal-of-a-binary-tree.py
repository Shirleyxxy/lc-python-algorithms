# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Time Complexity: O(NlogN)
## Space Complexity: O(N)
class Solution:
    def verticalTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        if not root: return []

        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)]) # node, x, depth

        while queue:
            node, x, depth = queue.popleft()
            cols[x].append((depth, node.val))
            if node.left:
                queue.append((node.left, x-1, depth+1))
            if node.right:
                queue.append((node.right, x+1, depth+1))

        res = []
        # from left to right
        for k in sorted(cols.keys()):
            # from top to bottom
            # if two nodes have the same position, report smaller value first
            col = [val[1] for val in sorted(cols[k])]
            res.append(col)
        return res
