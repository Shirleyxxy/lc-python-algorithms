# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Time Complexity: O(N)
## Space Complexity: O(N)
## Without None node + BST feature
class Codec:
    def preorder(self, node, lst):
        '''
        node --> left --> right.
        '''
        if not node: return
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

    ## Iterative deserialization using the property of BST
    def deserialize(self, data):
        '''
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        '''
        if not data: return None
        # root --> left subtree --> right subtree
        data = list(map(int, data.split(',')))
        stack = []
        # root 
        root = node = TreeNode(data[0])
        for val in data[1:]:
            # construct the left subtree
            if val < node.val:
                node.left = TreeNode(val)
                stack.append(node)
                node = node.left
            # construct the right subtree
            else:
                while stack and stack[-1].val < val:
                    node = stack.pop()
                node.right = TreeNode(val)
                node = node.right
        return root
