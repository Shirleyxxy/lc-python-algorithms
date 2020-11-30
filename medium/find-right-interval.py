## Solution 1 - Brute force
## Time: O(N^2)
## The complete set of N intervals is scanned for every (N) interval chosen.


## Solution 2 - Sorting + Linear scan
## Time: O(N^2)


## Solution 3 - Sorting + Binary search
## Time Complexity: O(NlogN)
## Space Complexity: O(N)
class Solution:
    def binarySearch(self, end, arr, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid][1][0] == end:
                return mid
            elif arr[mid][1][0] > end:
                right = mid
            else:
                left = mid + 1
        return left

    def findRightInterval(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: List[int]
        '''
        dic = {i:interval for i, interval in enumerate(intervals)}
        dic = sorted(dic.items(), key = lambda x: x[1][0])
        res = [float('-inf')] * len(intervals)

        for i, item in enumerate(dic):
            idx, interval = item[0], item[1]
            ans = self.binarySearch(interval[1], dic, i+1, len(dic))
            if ans == len(dic):
                res[idx] = -1
            else:
                res[idx] = dic[ans][0]
        return res


## Solution 4 - Two heaps
## Time Complexity: O(NlogN)
## Space Complexity: O(N)
class Solution:
    def findRightInterval(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: List[int]
        '''
        result = [-1] * len(intervals)
        max_start_heap, max_end_heap = [], []
        for i in range(len(intervals)):
            heappush(max_start_heap, (-intervals[i][0], i))
            heappush(max_end_heap, (-intervals[i][1], i))

        # go through all the intervals to find each interval's next interval
        for _ in range(len(intervals)):
            top_end, i = heappop(max_end_heap)
            if max_start_heap and -max_start_heap[0][0] >= -top_end:
                curr_start, curr_start_i = heappop(max_start_heap)
                # keep finding the interval that has the closest start
                while max_start_heap and -max_start_heap[0][0] >= -top_end:
                    curr_start, curr_start_i = heappop(max_start_heap)
                result[i] = curr_start_i
                # put the interval back as it could be the next interval of other intervals
                heappush(max_start_heap, (curr_start, curr_start_i))
        return result
