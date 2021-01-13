# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Recursive
## Time Complexity: O(N)
## Space Complexity: O(N)
## N is the number of overlapping nodes between the two trees
class Solution:
    def mergeTrees(self, t1, t2):
        '''
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        '''
        if not t1 and not t2: return None
        if not t1: return t2
        if not t2: return t1

        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node


## Iterative
## Time Complexity: O(N)
## Space Complexity: O(N)
## N is the smaller of the number of nodes in the two trees
class Solution:
    def mergeTrees(self, t1, t2):
        '''
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        '''
        if not t1: return t2
        queue = collections.deque([(t1, t2)])
        while queue:
            n1, n2 = queue.popleft()
            if not n2: continue
            n1.val += n2.val
            if not n1.left:
                n1.left = n2.left
            else:
                queue.append((n1.left, n2.left))

            if not n1.right:
                n1.right = n2.right
            else:
                queue.append((n1.right, n2.right))

        return t1
