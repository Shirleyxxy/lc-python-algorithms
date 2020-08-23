## Requirement: perform all the operations in O(1) time complexity.
## Basic idea: key --> val (using map) --> keys (val:set of keys)
## Bag class contains the set of all keys of a given value. Blocks form
## a DoubleLinkedList to maintain the order of the values.
## Use a dictionary to find the block of a given key.

class Bag():
    '''
    val -> keys set.
    '''
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev, self.next = None, None

    def insert_after(self, new_bag):
        old_next = self.next
        self.next = new_bag
        new_bag.prev = self
        new_bag.next = old_next
        old_next.prev = new_bag


class AllOne:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.head = Bag() # dummy head
        self.tail = Bag() # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping = {} # key --> bag mapping


    def inc(self, key):
        '''
        :type key: str
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        '''
        # find the current bag
        if not key in self.mapping:
            curr_bag = self.head
        else:
            curr_bag = self.mapping[key]
            # remove the key from the current bag
            curr_bag.keys.remove(key)

        # find / create the new bag
        if curr_bag.val + 1 != curr_bag.next.val:
            new_bag = Bag(curr_bag.val+1)
            curr_bag.insert_after(new_bag)
        else:
            new_bag = curr_bag.next

        # update the new bag and the mapping
        new_bag.keys.add(key)
        self.mapping[key] = new_bag

        # delete the current bag if it is not dummy head and it becomes empty
        if not curr_bag.keys and curr_bag.val != 0:
            curr_bag.remove()


    def dec(self, key):
        '''
        :type key: str
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        '''
        if not key in self.mapping: return

        # find the current bag
        curr_bag = self.mapping[key]
        # delete the mapping and remove the key from the current bag
        del self.mapping[key]
        curr_bag.keys.remove(key)

        if curr_bag.val != 1:
            # insert a new bag
            if curr_bag.val - 1 != curr_bag.prev.val:
                new_bag = Bag(curr_bag.val-1)
                curr_bag.prev.insert_after(new_bag)
            else:
                new_bag = curr_bag.prev
            new_bag.keys.add(key)
            self.mapping[key] = new_bag

        # delete the current bag if it becomes empty
        if not curr_bag.keys:
            curr_bag.remove()


    def getMaxKey(self):
        '''
        :rtype: str
        Returns one of the keys with maximal value.
        '''
        if self.tail.prev.val == 0:
            return ''
        # pop then add back
        key = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(key)
        return key


    def getMinKey(self):
        '''
        :rtype: str
        Returns one of the keys with Minimal value.
        '''
        if self.head.next.val == 0:
            return ''
        # pop then add back
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key
