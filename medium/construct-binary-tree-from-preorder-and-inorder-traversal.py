# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Preorder: node --> left --> right, easy to construct the tree
## The first value in the preorder list is the value for the root
## We find the index of root value in the inorder list, and split
## the problem into two subproblems (build left & right subtrees).

## Recursion
## Time Complexity: O(N)
## Iterate each node once to recursively build the tree
## Space Complexity: O(N)
## Note: preorder is a mutable object (list). Since we are building the left subtree first
## the elements for it will be extracted out before building the right subtree.

class Solution:
    def buildTree(self, preorder, inorder):
        '''
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        '''
        if inorder:
            root_idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_idx])
            root.left = self.buildTree(preorder, inorder[:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx+1:])
            return root


## Two Optimizations
## 1. Use left and right pointers rather than slicing (copying) inorder list when building subtrees
## 2. Use dictionary to store the indexes of the elements in the inorder list to avoid searching every time
## O(N) time complexity for list.index(x)

class Solution:
    def buildTree(self, preorder, inorder):
        '''
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        '''
        inorder_d = {val:i for i, val in enumerate(inorder)}
        return self.dfs(inorder_d, preorder, 0, len(inorder)-1)

    def dfs(self, inorder_d, preorder, in_left, in_right):
        if in_left > in_right: return None
        root_val = preorder.pop(0)
        root_idx = inorder_d[root_val]
        root = TreeNode(root_val)
        root.left = self.dfs(inorder_d, preorder, in_left, root_idx-1)
        root.right = self.dfs(inorder_d, preorder, root_idx+1, in_right)
        return root
