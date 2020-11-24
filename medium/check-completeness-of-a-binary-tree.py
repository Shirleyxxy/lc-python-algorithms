# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## BFS (Level order traversal)
## Time Complexity: O(N)
## Space Complexity: O(N)
## The tree is complete if the codes representing the positions of the nodes
## take the form of [1,2,3,4,...] in sequence with no gaps.

class Solution:
    def isCompleteTree(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        if not root: return True
        queue = collections.deque([(root, 1)])
        res = []
        while queue:
            node, i = queue.popleft()
            res.append(i)
            if node.left:
                queue.append((node.left, 2*i))
            if node.right:
                queue.append((node.right, 2*i+1))
        return len(res) == res[-1]


## BFS (Level order traversal)
## Time Complexity: O(N)
## Space Complexity: O(N)
## The tree is complete if there are no nodes after the first empty node we encounter.
class Solution:
    def isCompleteTree(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        nodes = [root]
        i = 0
        while nodes[i]:
            nodes.append(nodes[i].left)
            nodes.append(nodes[i].right)
            i += 1
        return not any(nodes[i:])
