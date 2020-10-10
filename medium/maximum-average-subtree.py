# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Time Complexity: O(N)
## Space Complexity: O(N) for avg_list, O(H) for recursion stack, overall O(N)

class Solution:
    def maximumAverageSubtree(self, root):
        '''
        :type root: TreeNode
        :rtype: float
        '''
        avg_list = []
        self.dfs(root, avg_list)
        return max(avg_list)


    def dfs(self, node, avg_list):
        if not node: return (0, 0)
        left_sum, left_cnt = self.dfs(node.left, avg_list)
        right_sum, right_cnt = self.dfs(node.right, avg_list)
        _sum = left_sum + right_sum + node.val
        _cnt = left_cnt + right_cnt + 1
        avg = _sum/_cnt
        avg_list.append(avg)
        return (_sum, _cnt)


## avg_list is not necessary; we can keep updating the max during the recursive process
## Time Complexity: O(N)
## Space Complexity: O(H)

class Solution:
    def maximumAverageSubtree(self, root):
        '''
        :type root: TreeNode
        :rtype: float
        '''
        def dfs(node):
            if not node: return (0, 0)
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            _sum = left_sum + right_sum + node.val
            _cnt = left_cnt + right_cnt + 1
            self.max_avg = max(self.max_avg, _sum/_cnt)
            return (_sum, _cnt)

        self.max_avg = float('-inf')
        dfs(root)
        return self.max_avg
