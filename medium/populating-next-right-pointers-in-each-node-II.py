"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## Solution 1 - Level order traversal
## Time Complexity: O(N)
## Space Complexity: O(N)
from collections import deque

class Solution:
    def connect(self, root):
        '''
        :type root: Node
        :rtype: Node
        '''
        if not root: return root 

        queue = deque()
        queue.append(root)
        # Outer while loop which iterates over each level
        while queue:
            prev_node, level_size = None, len(queue)
            # the size of the queue always corresponds to
            # all the nodes on a particular level
            for _ in range(level_size):
                curr_node = queue.popleft()
                if prev_node:
                    prev_node.next = curr_node
                prev_node = curr_node

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return root


## Solution 2 - Using previously established next pointers
## curr: variable we use to traverse all the nodes on the current level
## prev: latest node on the next level

## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def process_child(self, child, prev, leftmost):
        if child:
            # already found at least one node on the next level
            if prev:
                prev.next = child
            # this child node is the first node on the next level
            else:
                leftmost = child
            prev = child
        return prev, leftmost

    def connect(self, root):
        '''
        :type root: Node
        :rtype: Node
        '''
        if not root: return root
        leftmost = root
        # we have no idea about the structure of the tree
        # so we keep going until we find the last level.
        # The nodes on the last level won't have any children.
        while leftmost:
            prev, curr = None, leftmost
            # reset this so that we can re-assign it to the leftmost node of the next level
            # also, if there isn't one, this would help break us out of the outmost loop
            leftmost = None
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
        return root
