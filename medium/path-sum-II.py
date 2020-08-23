## Time Complexity: O(N^2)
## Space Complexity: O(N) in the worst case if we ignore the space required for the all_paths list.
## This space will be used to store the recursion stack. The worst case will happen when the given
## tree is a linked list. 

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
        :rtype: List[List[int]]
        '''
        all_paths = []
        self.dfs(root, sum, [], all_paths)
        return all_paths


    def dfs(self, curr_node, remaining_sum, curr_path, all_paths):
        if curr_node:
            if not curr_node.left and not curr_node.right and curr_node.val == remaining_sum:
                all_paths.append(curr_path + [curr_node.val])
            self.dfs(curr_node.left, remaining_sum - curr_node.val, curr_path + [curr_node.val], all_paths)
            self.dfs(curr_node.right, remaining_sum - curr_node.val, curr_path + [curr_node.val], all_paths)
