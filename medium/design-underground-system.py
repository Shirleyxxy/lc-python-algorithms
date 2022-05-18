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

## Data structure: one regular dictionary + one defaultdict(list)
## How does Python store dictionaries?
## hash table: <hash, key, value>
## hash collisions: random probing for an empty slot

## Python's dictionary implementation reduces the average complexity of dictionary lookups to O(1)
## by requiring that key objects provide a "hash" function. Such a hash function takes the information
## in a key object and uses it to produce an integer, called a hash value.
## This hash value is then used to determine which "bucket" this (key, value) pair should be placed into.

## What key types can be used in Python?
## A dictionary key must be of a type that is immutable!
## We can use an integer, float, string, boolean or tuple as dictionary key.
## A list cannot be served as a dictionary key! (lists and dictionaries are mutable)

## Follow-up Questions:
## What if a person lost his card?
## Checked in, but never checked out? (==> Clean the invalid data in the db periodically)
## Multiple checked in (==> override the previous data)
## How to calculate the average time if the number of passengers making a journey at the same time is very large?
## (==> MapReduce?)


class UndergroundSystem:
    def __init__(self):
        # save the check-in time and station for a user
        # one entry for each passenger who has checked in, but not checked out
        # only contains the current check-in data
        self.users = {}
        # record the times spent between two stations
        self.travels = collections.defaultdict(list)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.users[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station, start_time = self.users[id]
        self.travels[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return float(
            sum(self.travels[(startStation, endStation)])
            / len(self.travels[(startStation, endStation)])
        )
