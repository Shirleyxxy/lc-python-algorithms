"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


## Solution 1 - level order traversal, more straightforward
## time complexity: O(N)
## space complexity: O(N)

from collections import deque


class Solution:
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = deque()
        queue.append(root)
        # outer while loop which iterates over each level
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


## Solution 2 - pointers, more space optimized
## time complexity: O(N)
## space complexity: O(1)


class Solution:
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        node = root

        while node:
            # create a dummy leftmost node for the next (child) level
            dummy = Node(0)
            curr = dummy
            # while nodes exist on the parent level
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next

            # move to the next level
            # at the beginning of each iteration of the outer loop
            # curr and dummy both point at the same direction in memory

            # thus, when curr.next is updated for the first time inside the inner loop
            # dummy.next effectively points to the first node on the next level
            node = dummy.next

        return root
