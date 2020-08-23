"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## Solution 1 - Level order traversal (BFS)
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
## We establish the next pointers for a level N while we are still on level
## N-1.

## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def connect(self, root):
        '''
        :type root: Node
        :rtype: Node
        '''
        if not root: return root
        leftmost = root
        # once we reach the final level, we are done
        while leftmost.left:
            head = leftmost
            while head:
                # connection 1
                head.left.next = head.right
                # connection 2
                if head.next:
                    head.right.next = head.next.left
                # progress along the nodes on the current level
                head = head.next
            # Move onto the next level
            leftmost = leftmost.left
        return root
