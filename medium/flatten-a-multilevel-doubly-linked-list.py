"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

## solution 1 - Preorder DFS using recursion
## (really hard to code)
## child: left pointer in binary tree
## next: right pointer in binary tree

## time Complexity: O(N) - DFS traverses each node once and only once
## space Complexity: O(N) in the worst case - nodes are chained with each other
## only with the child pointers
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        # use pseudo_head to ensure the prev pointer is never None
        # reduce the null pointer checks
        pseudo_head = Node(None, None, head, None)
        self.flatten_dfs(pseudo_head, head)
        # detach the pseudo_head from the real head
        pseudo_head.next.prev = None
        return pseudo_head.next

    def flatten_dfs(self, prev, curr):
        """
        Return the tail of the flattened list.
        """
        if not curr:
            return prev
        curr.prev = prev
        prev.next = curr
        # the curr.next would be tempered in the recursive function
        temp_next = curr.next
        # equivalent to flatten the left subtree
        tail = self.flatten_dfs(curr, curr.child)
        # remove the child pointer since it is no longer needed in the final result
        curr.child = None
        # equivalent to flatten the right subtree
        return self.flatten_dfs(tail, temp_next)


## solution 2 - Preorder DFS using stack
## time Complexity: O(N)
## space Complexity: O(N) additional space
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack, order = [head], []

        while stack:
            curr = stack.pop()
            order.append(curr)
            # put next first, then child because we want to
            # visit child and then next
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
        # rebuild the doubly linked list from our order list
        for i in range(len(order) - 1):
            order[i].next = order[i + 1]
            order[i + 1].prev = order[i]
            order[i].child = None

        order[len(order) - 1].child = None
        return order[0]


## solution 3 - Preorder DFS using stack & optimized space
## time complexity: O(N)
## space complexity: O(logN) on average, O(N) in the worst case
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack = [head]
        # dummy node
        prev = Node(0, None, None, None)
        while stack:
            curr = stack.pop()
            # put next first, then child because we want to
            # visit child and then next
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            prev.next = curr
            curr.prev = prev
            curr.child = None
            prev = curr
        # detach from the dummy node
        head.prev = None
        return head
