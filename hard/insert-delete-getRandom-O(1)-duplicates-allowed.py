## Dictionary + List
## Time Complexity: O(1) for all operations
## Space Complexity: O(N)
class RandomizedCollection:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.vals = []
        self.val2idx = collections.defaultdict(set)


    def insert(self, val):
        '''
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        '''
        self.val2idx[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.val2idx[val]) == 1


    def remove(self, val):
        '''
        Removes a value from the collection. Returns true if the collection contained the specified element.
        '''
        if self.val2idx[val]:
            out_idx = self.val2idx[val].pop()
            last = self.vals[-1]
            self.vals[out_idx] = last
            # update the dictionary
            self.val2idx[last].add(out_idx)
            self.val2idx[last].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False


    def getRandom(self):
        '''
        Get a random element from the collection.
        '''
        return random.choice(self.vals)
