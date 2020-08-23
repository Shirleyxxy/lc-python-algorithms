# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## Recursive Solution
## Time Complexity: O(N)
## Space Complexity: worst case - O(N); average case - O(logN)
class Solution:
    def inorderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: List[int]
        left -> node -> right
        '''
        res = []
        self.inorder_rec(root, res)
        return res

    def inorder_rec(self, node, res):
        if node:
            self.inorder_rec(node.left, res)
            res.append(node.val)
            self.inorder_rec(node.right, res)


## Iterative Solution
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def inorderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: List[int]
        left -> node -> right
        '''
        stack, res = [], []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


## Iterative solution using a visited flag
## Visited flag is used since for inorder traversal, we do not want to
## process the node value (append to the result list here) when we see it
## for the first time.
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def inorderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: List[int]
        left -> node -> right
        '''
        stack, res = [(root, False)], []
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    # process order: left --> curr --> right
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
        return res
