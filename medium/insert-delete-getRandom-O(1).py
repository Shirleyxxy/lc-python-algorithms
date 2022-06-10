## dictionary + list
## dictionary provides insert & delete in average constant time
## but has problems with getRandom
## list has indexes and provides getRandom in average constant time

## dictionary stores value --> its index mapping
## to delete a value at arbitrary index takes linear time
## the solution is to always delete the last value
#### swap the element to delete with the last one
#### pop the last element out


## time complexity: average O(1) for all operations
## space complexity: O(N)


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d, self.vals = {}, []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val] = len(self.vals)
            self.vals.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            idx = self.d[val]
            last = self.vals[-1]
            self.d[last] = idx  # overwrite the index for the last element
            self.vals[idx] = last  # move the last element to the new position
            self.vals.pop()
            del self.d[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.vals)
