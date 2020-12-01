## My first attempt (Brute force)
## Counter / Dictionary
## Time Limit Exceeded
## K = the length of the initial array passed into the constructor
## N = the total number of items added onto the queue so far

## Time Complexity: O(K) for constructor; O(1) for add; O(N) for showFirstUnique
## Space Complexity: O(N)

from collections import deque, defaultdict
class FirstUnique:
    def __init__(self, nums):
        '''
        :type nums: List[int]
        '''
        self.queue = deque(nums)
        self.freq_dict = defaultdict(int)
        for num in self.queue:
            self.freq_dict[num] += 1

    def showFirstUnique(self):
        '''
        :rtype: int
        '''
        for num in self.queue:
            if self.freq_dict[num] == 1:
                return num
        return -1

    def add(self, value):
        '''
        :type value: int
        :rtype: None
        '''
        self.queue.append(value)
        self.freq_dict[value] += 1


## Interviewer: What if we need to call showFirstUnique frequently
## and the list of numbers is very long (N is large)?
## Set + Dictionary
## We can use OrderedDict since we need to keep track of the order of the unique numbers.
## However, normal dictionary in Python >= 3.6 preserves the insertion order, so we can easily get the first element
## by iterating it.

## Time Complexity: O(K) for constructor; O(1) for add and showFirstUnique
## Space Complexity: O(N)
class FirstUnique:
    def __init__(self, nums):
        '''
        :type nums: List[int]
        '''
        self.added = set()
        self.unique_nums = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        '''
        :rtype: int
        '''
        # for key in self.unique_nums.keys():
        #     return key
        # return -1
        return next(iter(self.unique_nums), -1)

    def add(self, value):
        '''
        :type value: int
        :rtype: None
        '''
        if value not in self.added:
            self.added.add(value)
            self.unique_nums[value] = True
        else:
            if value in self.unique_nums:
                del self.unique_nums[value]


## Same as above - use OrderedDict as an ordered set
from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums):
        '''
        :type nums: List[int]
        '''
        self.added = set()
        self.unique_nums = OrderedDict()
        for num in nums:
            self.add(num)


    def showFirstUnique(self):
        '''
        :rtype: int
        '''
        for key in self.unique_nums.keys():
            return key
        return -1


    def add(self, value):
        '''
        :type value: int
        :rtype: None
        '''
        if value not in self.added:
            self.added.add(value)
            self.unique_nums[value] = True
        else:
            if value in self.unique_nums:
                del self.unique_nums[value]
