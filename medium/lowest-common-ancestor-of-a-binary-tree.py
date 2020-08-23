# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Recursive solution
## Time Complexity: O(N)
## Space Complexity: O(N)
## In the worst case we might be visiting all the nodes of the binary tree.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        '''
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        '''
        if not root: return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left


## Iterative solution
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        '''
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        '''
        if not root: return None
        queue = collections.deque([root])
        # dictionary for parent pointers
        parent = {root:None}
        # Iterate until we find both q and q
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
        # Process all ancestors for node p using parent pointers
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        # The first ancestor of q which appears in p's ancestors is their
        # lowest common ancestor
        while q not in ancestors:
            q = parent[q]
        return q
