## Dictionary + List
## Time Complexity: O(1)
## Space Complexity: O(N)

class RandomizedSet:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.d, self.vals = {}, []


    def insert(self, val):
        '''
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        '''
        if val not in self.d:
            self.d[val] = len(self.vals)
            self.vals.append(val)
            return True
        return False


    def remove(self, val):
        '''
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        '''
        if val in self.d:
            # swap the element to delete with the last one
            idx, last = self.d[val], self.vals[-1]
            self.vals[idx], self.d[last] = last, idx
            # pop the last element out
            self.vals.pop()
            del self.d[val]
            return True
        return False


    def getRandom(self):
        '''
        Get a random element from the set.
        :rtype: int
        '''
        return random.choice(self.vals)
