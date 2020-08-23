## Time Complexity: O(N^2) in the worst case; O(NlogN) in the best case
## Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, sum):
        '''
        :type root: TreeNode
        :type sum: int
        :rtype: int
        '''
        if not root: return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, curr_node, target_sum):
        if not curr_node: return 0
        return (curr_node.val == target_sum) + self.dfs(curr_node.left, target_sum - curr_node.val) + self.dfs(curr_node.right, target_sum - curr_node.val)
