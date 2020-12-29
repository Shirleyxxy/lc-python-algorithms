## Recursive solution
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def isSymmetric(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        if not root: return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)



## Iterative solution
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def isSymmetric(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        if not root: return True
        queue = collections.deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True
