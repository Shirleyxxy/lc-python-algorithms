## column-wise order - based on its relative offset to the root node of the tree
## row-wise order - based on its level (guaranteed by the BFS traversal)
## Modified level order traversal

## Time Complexity: O(NlogN) - N is the number of nodes in the tree
## Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root):
        '''
        :type root: TreeNode
        :rtype: List[List[int]]
        '''
        if not root: return []
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))

        # sort the obtained dictionary by its keys
        return [cols[k] for k in sorted(cols.keys())]
