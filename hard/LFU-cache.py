## OrderedDict: dictionary + doubly linkedlist
## Idea: create a dictionary of OrderedDicts self.freq2nodes
## self.min_freq takes care of the least frequently used items
## O(1) to access the corresponding OrderedDict
## OrderedDict takes care of the order
## O(1) to update / remove the least recently used key

## Tricky part is to make sure we update self.key2node, self.freq2nodes, and self.min_freq
## correctly once we call get and put.

from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key2node = {}
        self.freq2nodes = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        '''
        Time: O(1).
        '''
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.freq2nodes[node.freq][key]

        ## clean memory once the ordered dict is empty
        if not self.freq2nodes[node.freq]:
            del self.freq2nodes[node.freq]

        node.freq += 1
        self.freq2nodes[node.freq][key] = node

        # update min_freq
        if not self.freq2nodes[self.min_freq]:
            self.min_freq += 1

        return node.val


    def put(self, key, value):
        '''
        Time: O(1).
        '''
        ## edge case: cannot put any item
        if not self.capacity:
            return
        ## case 1 - update a node
        if key in self.key2node:
            self.key2node[key].val = value
            ## equivalent to access it
            self.get(key)
            ## done
            return

        ## case 2 - add a new node
        if len(self.key2node) == self.capacity:
            k, node = self.freq2nodes[self.min_freq].popitem(last = False)
            del self.key2node[k]

        self.key2node[key] = Node(key, value, 1)
        self.freq2nodes[1][key] = Node(key, value, 1)
        self.min_freq = 1
        return
