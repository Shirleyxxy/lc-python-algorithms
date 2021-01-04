# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Solution 1 - Recursion
## Time Complexity: O(N)
## Space Complexity: O(logN) in the best case; O(N) in the worst case
class Solution:
    def isSameTree(self, p, q):
        '''
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        '''
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



## Solution 2 - Iteration
## Time Complexity: O(N)
## Space Complexity: O(logN) in the best case; O(N) in the worst case
from collections import deque
class Solution:
    def isSameTree(self, p, q):
        '''
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        '''
        queue = deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            elif not n1 or not n2 or n1.val != n2.val:
                return False
            else:
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
        return True
