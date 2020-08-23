## Dictionary + Binary Search
## Time Complexity: O(1) for set; O(logN) for get
## Space Complexity: O(N)

class TimeMap:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.d = collections.defaultdict(list)


    def set(self, key, value, timestamp):
        '''
        Stores the key and value, along with the given timestamp.
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        '''
        self.d[key].append((timestamp, value))


    def get(self, key, timestamp):
        '''
        Modified binary search for the largest timestamp less than or equal to
        the given timestamp.
        :type key: str
        :type timestamp: int
        :rtype: str
        '''
        if key not in self.d:
            return ''
        lst = self.d[key]
        start, end = 0, len(lst)-1
        while start <= end:
            mid = start + (end - start) // 2
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            elif lst[mid][0] < timestamp:
                start = mid + 1
            else:
                end = mid - 1
        return lst[end][1] if lst[end][0] <= timestamp else ''


## Same idea using bisect
## Time Complexity: O(1) for set; O(logN) for get
## Space Complexity: O(N)

class TimeMap:
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.timestamps = collections.defaultdict(list)
        self.values = collections.defaultdict(list)


    def set(self, key, value, timestamp):
        '''
        Stores the key and value, along with the given timestamp.
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        '''
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)


    def get(self, key, timestamp):
        '''
        :type key: str
        :type timestamp: int
        :rtype: str
        '''
        # use bisect_right to find the rightmost value less than or equal to timestamp
        i = bisect.bisect_right(self.timestamps[key], timestamp)
        # i is the index at which the particular timestamp can be inserted and still maintain the order
        # so the rightmost value less than or equal to timestamp is located at i-1
        return self.values[key][i-1] if i else ''
