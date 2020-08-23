"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

## Solution 1 - DFS
## Time Complexity: O(N)
## Space Complexity: O(N)
class Codec:
    def preorder(self, node, lst):
        if not node: return
        lst.append(str(node.val))
        for child in node.children:
            self.preorder(child, lst)
        lst.append('#')


    def serialize(self, root):
        '''
        Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        '''
        res = []
        self.preorder(root, res)
        return ','.join(res)


    def deserialize(self, data):
        '''
        Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        '''
        if not data: return None
        nodes = data.split(',')
        root = Node(int(nodes.pop(0)), [])

        def deserialize_rec(node):
            # add child nodes with subtrees
            while nodes[0] != '#':
                child = Node(int(nodes.pop(0)), [])
                node.children.append(child)
                deserialize_rec(child)
            # discard the '#'
            nodes.pop(0)

        deserialize_rec(root)
        return root



## Solution 2 - BFS
## Time Complexity: O(N)
## Space Complexity: O(N)
from collections import deque

class Codec:
    def serialize(self, root):
        '''
        Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        '''
        if not root: return ''
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node != '#':
                res.append(str(node.val))
                for child in node.children:
                    queue.append(child)
                queue.append('#')
            else:
                res.append('#')
        return ','.join(res)


    def deserialize(self, data):
        '''
        Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        '''
        if not data: return None
        nodes = data.split(',')
        root = Node(int(nodes[0]), [])
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            while nodes[idx] != '#':
                child = Node(int(nodes[idx]), [])
                node.children.append(child)
                queue.append(child)
                idx += 1
            idx += 1
        return root
