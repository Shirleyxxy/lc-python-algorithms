"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## Solution 1 - level order traversal (BFS)
## time complexity: O(N)
## space complexity: O(N)


class Solution:
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = collections.deque([root])
        # outer while loop which iterates over each level
        while queue:
            prev, level_size = None, len(queue)
            # the size of the queue always corresponds to
            # all the nodes on a particular level
            for _ in range(level_size):
                curr = queue.popleft()
                if prev:
                    prev.next = curr
                prev = curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root


## Solution 2 - pointers
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

        leftmost = root
        # once we reach the final level, we are done
        while leftmost.left:
            curr = leftmost
            while curr:
                # connection 1
                curr.left.next = curr.right
                # connection 2
                if curr.next:
                    curr.right.next = curr.next.left
                # progress along the nodes on the current level
                curr = curr.next
            # move onto the next level
            leftmost = leftmost.left
        return root
