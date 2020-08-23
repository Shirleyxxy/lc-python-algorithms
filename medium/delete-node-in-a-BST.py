## 3 facts about BST
## 1. Inorder traversal of BST is an array sorted in the ascending order (left --> node --> right).
## 2. Successor = the smallest node after the current node
## To find the successor: go to right once and then as many times to the left as you could
## 3. Predecessor = the largest node before the current node
## To find the predecessor: go to left once and then as many times to the right as you could

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Time Complexity: O(logN) for balanced trees
## O(H1) to search the node to delete; H1 is the tree height from root to the node to delete
## O(H2) to delete; H2 is the tree height from the node to delete to the leaf
## O(H1 + H2) = O(H), where H is a tree height
## Space Complexity: O(H) to keep the recursion stack

class Solution:
    def successor(self, node):
        '''
        One step right and then always left.
        Return the value of the successor node.
        '''
        node = node.right
        while node.left:
            node = node.left
        return node.val


    def predecessor(self, node):
        '''
        One step left and then always right.
        Return the value of the predecessor node.
        '''
        node = node.left
        while node.right:
            node = node.right
        return node.val


    def deleteNode(self, root, key):
        '''
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        '''
        if not root: return None
        # delete from the right subtree
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not root.left and not root.right:
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                # proceed down to recursively delete the successor
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf and has no right child (has a left child)
            else:
                root.val = self.predecessor(root)
                # proceed down to recursively delete the predecessor
                root.left = self.deleteNode(root.left, root.val)
        return root
