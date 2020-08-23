# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Recursive solution
## Time Complexity: O(N)
## Space Complexity: O(N) in the worst case
class Solution:
    def flatten(self, root):
        '''
        Do not return anything, modify root in-place instead.
        :type root: TreeNode
        :rtype: None
        '''
        self.flatten_dfs(root)

    def flatten_dfs(self, node):
        if not node: return None
        # for a leaf node, we return the node as is
        if not node.left and not node.right:
            return node
        # recursively flatten the left subtree
        left_tail = self.flatten_dfs(node.left)
        # recursively flatten the right subtree
        right_tail = self.flatten_dfs(node.right)

        # if there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side.
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        # need to return the "rightmost" node after we are done
        # wiring the new connections
        return right_tail if right_tail else left_tail


## Iterative solution using stack
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def flatten(self, root):
        '''
        Do not return anything, modify root in-place instead.
        :type root: TreeNode
        :rtype: None
        '''
        if not root: return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            node.right = stack[-1] if stack else None
