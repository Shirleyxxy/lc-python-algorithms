## Assumption:
## A customer can only be checked into one place at a time.

## Time Complexity: O(1) for checkIn, checkOut, getAverageTime
## Space Complexity: O(P + S^2)
## P: the maximum possible number of passengers making a journey at the same time
## S: the number of stations
## Over time, we could expect every possible pair of the S stations
## on the network to have an entry in the dictionary.
## As we don't know whether S^2 or P is larger, we need to add these
## together, giving a total space complexity of O(P + S^2).


class UndergroundSystem:

    def __init__(self):
        # save the check-in time and station for a user
        # one entry for each passenger who has checked in, but not checked out
        self.user = collections.defaultdict(list)
        # record the times spent between two stations
        self.stations = collections.defaultdict(list)


    def checkIn(self, id, stationName, t):
        '''
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        '''
        self.user[id] = [stationName, t]


    def checkOut(self, id, stationName, t):
        '''
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        '''
        start_station, start_time = self.user[id]
        self.stations[(start_station, stationName)].append(t - start_time)


    def getAverageTime(self, startStation, endStation):
        '''
        :type startStation: str
        :type endStation: str
        :rtype: float
        '''
        return float(sum(self.stations[(startStation, endStation)]) / len(self.stations[(startStation, endStation)]))
