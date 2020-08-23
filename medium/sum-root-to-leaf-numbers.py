## Recursive Preorder Traversal
## Node (update sum) --> Left (recursive calls) --> Right (recursive calls)
## Time Complexity: O(N)
## Space Complexity: O(H) to keep the recursion stack, where H is a tree height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        return self.root_to_leaf(root, 0)

    def root_to_leaf(self, curr_node, curr_sum):
        if not curr_node: return 0
        curr_sum = 10 * curr_sum + curr_node.val
        if not curr_node.left and not curr_node.right:
            return curr_sum
        return self.root_to_leaf(curr_node.left, curr_sum) + self.root_to_leaf(curr_node.right, curr_sum)


## Iterative Preorder Traversal
## Stack
## Time Complexity: O(N)
## Space Complexity: O(H) to keep the stack, where H is a tree height.

class Solution:
    def sumNumbers(self, root):
        if not root: return 0
        stack, total_sum = [(root, root.val)], 0

        while stack:
            node, curr_sum = stack.pop()
            if node:
                if not node.left and not node.right:
                    total_sum += curr_sum
                if node.right:
                    stack.append((node.right, 10 * curr_sum + node.right.val))
                if node.left:
                    stack.append((node.left, 10 * curr_sum + node.left.val))
        return total_sum
