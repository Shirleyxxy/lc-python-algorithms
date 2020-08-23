## Solution 1
## Similar Problems: Merge Intervals
## Time Complexity: O(N * logN), N is the number of intervals
## Space Complexity: O(N) for sorting

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule):
        '''
        :type schedule: [[Interval]]
        :rtype: [Interval]
        '''
        if not schedule: return []
        # flatten the nested list then sort the intervals by start time
        intervals = sorted([int for sche in schedule for int in sche], key = lambda x: x.start)
        result, prev = [], intervals[0]
        for interval in intervals[1:]:
            # overlapping
            if interval.start <= prev.end and interval.end > prev.end:
                prev.end = interval.end
            # non-overlapping
            elif interval.start > prev.end:
                result.append(Interval(prev.end, interval.start))
                prev = interval
        return result


## Solution 2
## Time Complexity: O(N * logK), where K is the number of employees and N is the number of
## jobs across all employees. The max size of the heap is K, so each push and pop operation is
## O(logK) and there are O(N) such operations. 
## Space Complexity: O(K)

from heapq import *

class Solution:
    def employeeFreeTime(self, schedule):
        '''
        :type schedule: [[Interval]]
        :rtype: [Interval]
        '''
        if not schedule: return []
        result = []
        pq = [(intervals[0].start, emp_idx, 0) for emp_idx, intervals in enumerate(schedule)]
        heapify(pq)
        anchor = min(interval.start for intervals in schedule for interval in intervals)
        while pq:
            start_t, emp_idx, job_idx = heappop(pq)
            if anchor < start_t:
                result.append(Interval(anchor, start_t))
            anchor = max(anchor, schedule[emp_idx][job_idx].end)
            # add the next job for that employee
            if job_idx + 1 < len(schedule[emp_idx]):
                heappush(pq, (schedule[emp_idx][job_idx+1].start, emp_idx, job_idx+1))
        return result
