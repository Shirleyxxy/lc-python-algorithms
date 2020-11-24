## Time Complexity: O(N)
## Space Complexity: O(N) in the worst case to store the recursion stack

## The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        # global variable
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, curr_node):
        if not curr_node: return 0
        left = self.dfs(curr_node.left)
        right = self.dfs(curr_node.right)
        # update the diameter along the way
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1


class Solution:
    def diameterOfBinaryTree(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        self.diameter = 0
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter
