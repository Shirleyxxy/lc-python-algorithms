# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## BFS (Level by level traversal)
## Time Complexity: O(N) - We visit each node once and only once
## Space Complexity: O(N)
class Solution:
    def widthOfBinaryTree(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if not root: return 0
        max_width = 0
        curr_level = [(root, 0)]
        while curr_level:
            max_width = max(max_width, curr_level[-1][1] - curr_level[0][1] + 1)
            next_level = []
            for node, pos in curr_level:
                if node.left:
                    next_level.append((node.left, pos * 2))
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))
            curr_level = next_level
        return max_width


## DFS
## Time Complexity: O(N)
## Space Complexity: O(N) in the worst case
## self.left is O(|levels|), which is O(N) in the worst case
## The depth of the recursion would be O(N) as well in the worst case 
class Solution:
    def widthOfBinaryTree(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        # keep track of the position for the leftmost element per level
        self.left = {}
        self.max_width = 0

        def dfs(node, level, pos):
            if not node: return
            if level not in self.left:
                self.left[level] = pos
            self.max_width = max(self.max_width, pos - self.left[level] + 1)
            dfs(node.left, level + 1, pos * 2)
            dfs(node.right, level + 1, pos * 2 + 1)

        dfs(root, 0, 0)
        return self.max_width
