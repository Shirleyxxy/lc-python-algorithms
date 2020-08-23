## Time Complexity: O(N)
## Space Complexity: O(H), O(N) in the worst case 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, curr_node):
        if not curr_node: return 0
        # when we look at left and right branches of a node,
        # we only care about gains we can make
        # if the sum of all the nodes on the either of the branches
        # of a particular node is less than 0, that means that branch
        # is not worth exploring at all
        left = max(self.dfs(curr_node.left), 0)
        right = max(self.dfs(curr_node.right), 0)
        # update the global max_sum with the max_sum that involves curr_node as the root
        self.max_sum = max(self.max_sum, left + right + curr_node.val)
        # going back up the stack, we can only form a path involving the parent node
        # as the root with either of the branches
        return max(left, right) + curr_node.val
