"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#############
## Updated on Sep-19-2020
## Iterative solution
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def copyRandomList(self, head):
        '''
        :type head: Node
        :rtype: Node

        Mapping with old Nodes as keys and new Nodes as values.
        We create node's next and random as we iterate through the list from head to tail.
        defaultdict() is an efficient way of handling missing keys
        '''
        mapping = collections.defaultdict(lambda: Node(0, None, None))
        mapping[None] = None

        old_node = head
        while old_node:
            mapping[old_node].val = old_node.val
            mapping[old_node].next = mapping[old_node.next]
            mapping[old_node].random = mapping[old_node.random]
            old_node = old_node.next

        return mapping[head]



## Recursive solution
## Time Complexity: O(N)
## Space Complexity: O(N)

## 1. Start traversing the graph from head.
## 2. If we already have a cloned copy of the current node in the
## visited dictionary, we use the cloned node reference.
## 3. If we don't have a cloned copy in the visited dictionary,
## we create a new node and add it to the visited dictionary.
## 4. Make two recursive calls, one using the random pointer and the
## other using the next pointer.

#############
## Updated on Aug-16-2020
## More compact recursive (dfs) solution
class Solution:
    def copyRandomList(self, head):
        '''
        :type head: Node
        :rtype: Node
        '''
        visited = {}
        return self.dfs(head, visited)

    def dfs(self, node, d):
        if not node: return None
        if node in d:
            return d[node]
        clone = Node(node.val, None, None)
        d[node] = clone
        clone.next = self.dfs(node.next, d)
        clone.random = self.dfs(node.random, d)
        return clone


#############
class Solution:
    def __init__(self):
        # dictionary which holds old nodes as keys and new nodes as its values
        self.visited = {}

    def copyRandomList(self, head):
        '''
        :type head: Node
        :rtype: Node
        '''
        if not head: return None
        # already processed the current node
        if head in self.visited:
            return self.visited[head]
        # create a new node
        node = Node(head.val, None, None)
        self.visited[head] = node
        # recursively copy the remaining linked list
        # starting from the next pointer and the random pointer
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node



## Iterative solution
## Time Complexity: O(N) - one pass over the original linked list
## Space Complexity: O(N)
class Solution:
    def __init__(self):
        # dictionary which holds old nodes as keys and new nodes as its values
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        '''
        :type head: Node
        :rtype: Node
        '''
        if not head: return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # iterate on the linked list until all the nodes are cloned
        while old_node != None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            # move one step ahead in the linked list
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]
