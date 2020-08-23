## Binary Search + Two Pointers + Queue

## Time Complexity: O(logN + K) - O(logN) for binary search and O(K) for finding the 'K'
## closest numbers using the two pointers
## Space Complexity: O(1) if we ignore the space required for the output list

from collections import deque

class Solution:
    def binarySearch(self, arr, target):
        if target <= arr[0]: return 0
        if target >= arr[len(arr)-1]: return len(arr)-1

        start, end = 0, len(arr)-1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        # start == end + 1
        if target - arr[end] <= arr[start] - target:
            return end
        return start


    def findClosestElements(self, arr, k, x):
        '''
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        '''
        idx = self.binarySearch(arr, x)
        queue = deque()
        left, right = idx, idx + 1
        for i in range(k):
            if left >= 0 and right <= len(arr)-1:
                left_diff = abs(x - arr[left])
                right_diff = abs(x - arr[right])
                if left_diff <= right_diff:
                    queue.appendleft(arr[left])
                    left -= 1
                else:
                    queue.append(arr[right])
                    right += 1
            elif left >= 0:
                queue.appendleft(arr[left])
                left -= 1
            elif right <= len(arr)-1:
                queue.append(arr[right])
                right += 1
        return queue
