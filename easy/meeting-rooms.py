## Time Complexity: O(N * logN), dominated by sorting
## Space Complexity: O(N) for sorting 

class Solution:
    def canAttendMeetings(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: bool
        '''
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
