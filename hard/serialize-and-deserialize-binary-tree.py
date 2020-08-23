# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Solution 1 - DFS (Preorder)
## Time Complexity: O(N)
## Space Complexity: O(N)
class Codec:
    def preorder(self, node, lst):
        '''
        node --> left --> right.
        '''
        if not node:
            lst.append('#')
        else:
            lst.append(str(node.val))
            self.preorder(node.left, lst)
            self.preorder(node.right, lst)


    def serialize(self, root):
        '''
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        '''
        res = []
        self.preorder(root, res)
        return ','.join(res)


    def deserialize(self, data):
        '''
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        '''
        def deserialize_rec(lst):
            if lst[0] == '#':
                lst.pop(0)
                return None
            node = TreeNode(int(lst.pop(0)))
            node.left = deserialize_rec(lst)
            node.right = deserialize_rec(lst)
            return node

        lst = data.split(',')
        root = deserialize_rec(lst)
        return root


## Solution 2 - BFS
## Time Complexity: O(N)
## Space Complexity: O(N)

from collections import deque

class Codec:
    def serialize(self, root):
        '''
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        '''
        if not root: return ''
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            res.append(str(node.val) if node else '#')
        return ','.join(res)


    def deserialize(self, data):
        '''
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        '''
        if not data: return None
        lst = data.split(',')
        root = TreeNode(int(lst[0]))
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if lst[idx] != '#':
                node.left = TreeNode(int(lst[idx]))
                queue.append(node.left)
            idx += 1

            if lst[idx] != '#':
                node.right = TreeNode(int(lst[idx]))
                queue.append(node.right)
            idx += 1
        return root
