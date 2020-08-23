class MyHashMap:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.buckets = 1000
        self.itemsPerBucket = 1000
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def put(self, key, value):
        '''
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        '''
        hashkey = self.hash(key)
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None] * self.itemsPerBucket
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key):
        '''
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
        :type key: int
        :rtype: int
        '''
        hashkey = self.hash(key)
        if (not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:
            return -1
        return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key):
        '''
        Removes the mapping of the specified value key if this map contains a mapping for the key.
        :type key: int
        :rtype: void
        '''
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None


## Example:
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)

## Note:
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
