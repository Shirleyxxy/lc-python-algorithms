class MyHashMap(object):

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.hashmap = [[-1] * 1000 for _ in range(1000)]

    def put(self, key, value):
        '''
        Value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        '''
        row, col = key % 1000, key // 1000
        self.hashmap[row][col] = value

    def get(self, key):
        '''
        Returns the value to which the specified key is mapped, or -1 if this map contains
        no mapping for the key.
        '''
        row, col = key % 1000, key // 1000
        return self.hashmap[row][col]

    def remove(self, key):
        '''
        Removes the mapping of the specified value key if this map contains a mapping for the key.
        :type key: int
        :rtype: void
        '''
        row, col = key % 1000, key // 1000
        self.hashmap[row][col] = -1
