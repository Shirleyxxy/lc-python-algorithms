## Implement a data structure for Least Recently Used (LRU) cache
## Provide the following operations in O(1) time:
## Get the key / check if the key exists
## Put the key
## Delete the first added key

## OrderedDict are just like regular dictionaries but they remember the order that items were inserted.
## Algorithmically, OrderedDict can handle frequent reordering operations better than dict.
## This makes it suitable for tracking recent accesses (for example in an LRU cache).
## OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.
## The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
## The pairs are returned in LIFO order if last is true or FIFO order if false.


## Solution 1: OrderedDict
## Time Complexity: O(1) both for put & get
## Space Complexity: O(capacity)

from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity):
        '''
        :type capacity: int
        '''
        self.capacity = capacity

    def get(self, key):
        '''
        :type key: int
        :rtype: int
        Get the value of the key if the key exists in the cache,
        otherwise return -1.
        '''
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        '''
        :type key: int
        :type value: int
        :rtype: None
        Set or insert the value if the key is not already present.
        When the cache reached its capacity, it should invalidate
        the least recently used item before inserting a new item.
        '''
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)



## Solution 2: Dictionary + DoubleLinkedList
## There are pseudo head and pseudo tail to mark the boundary, so that we don't
## need to check the null node during the update.
## Time Complexity: O(1) both for put & get
## Space Complexity: O(capacity)

class DoubleLinkedListNode():
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None


class LRUCache():
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        # pseudo head & tail
        self.head = DoubleLinkedListNode(0, 0)
        self.tail = DoubleLinkedListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _add_node(self, node):
        '''
        Add the node to the end of the DoubleLinkedList.
        '''
        p_node = self.tail.prev
        p_node.next = node
        node.prev = p_node
        node.next = self.tail
        self.tail.prev = node


    def _remove_node(self, node):
        '''
        Remove the specified node from the DoubleLinkedList.
        '''
        p_node = node.prev
        n_node = node.next
        p_node.next = n_node
        n_node.prev = p_node


    def get(self, key):
        '''
        :type key: int
        :rtype: int
        Get the value of the key if the key exists in the cache,
        otherwise return -1.
        '''
        if key in self.cache:
            node = self.cache[key]
            # move the node to the end of the DoubleLinkedList
            self._remove_node(node)
            self._add_node(node)
            return node.value
        return -1


    def put(self, key, value):
        '''
        :type key: int
        :type value: int
        :rtype: None
        Set or insert the value if the key is not already present.
        When the cache reached its capacity, it should invalidate
        the least recently used item before inserting a new item.
        '''
        if key in self.cache:
            # update the node and move to the end
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_node(node)
        else:
            # create a new node and add at the end of the list
            node = DoubleLinkedListNode(key, value)
            self._add_node(node)
            # add the node to the cache dictionary
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                # remove the node at the beginning of the list
                node_to_remove = self.head.next
                self._remove_node(node_to_remove)
                # remove LRU node from the cache dictionary
                del self.cache[node_to_remove.key]
