# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Solution 1 - Recursion
## Time Complexity: O(N)
## Space Complexity: O(H), H is the height of the tree (recursion stack)
class Solution:
    def invertTree(self, root):
        '''
        :type root: TreeNode
        :rtype: TreeNode
        '''
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


## Solution 2 - Iterative solution
## Time Complexity: O(N) - each node in the tree is visited / added to the queue only once.
## Space Complexity: O(N) - in the worst case, the queue will contain all nodes in one level
## of the binary tree. For a full binary tree, the leaf level has N/2 = O(N) leaves.
class Solution:
    def invertTree(self, root):
        '''
        :type root: TreeNode
        :rtype: TreeNode
        '''
        if not root: return None
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
