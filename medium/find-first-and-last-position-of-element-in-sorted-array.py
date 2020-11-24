## Given an array of integers nums sorted in ascending order, find the starting
## and ending position of a given target value.
## Your algorithm's runtime complexity must be in the order of O(log n).
## If the target is not found in the array, return [-1, -1].

## My Solution (Binary Search)
## Time Complexity: O(logN)
## Space Complexity: O(1)
class Solution:
    def searchRange(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        if not nums or target > nums[-1]: return [-1, -1]
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                s, e = mid-1, mid+1
                while s >= 0 and nums[s] == target:
                    s -= 1
                while e <= len(nums)-1 and nums[e] == target:
                    e += 1
                return [s+1, e-1]
        return[-1, -1]


## Binary Search
class Solution(object):
    def searchRange(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        if len(nums) == 0:
            return [-1, -1]
        min, max = 0, len(nums)-1
        while min <= max:
            m = (min + max) // 2
            if nums[m] > target:
                max = m - 1
            elif nums[m] < target:
                min = m + 1
            # nums[m] == target
            else:
                for i in range(min, max + 1):
                    if nums[i] == target:
                        if min < i and nums[min] != nums[i]:
                            min = i
                        max = i
                return [min, max]
        return [-1, -1]


## Linear Scan (Time Complexity O(N))
## The break statement breaks out of the innermost enclosing for or while loop.
## Loop statements may have an else clause; it is executed when the loop terminates
## through exhaustion of the list (with for) or when the condition becomes false
## (with while), but not when the loop is terminated by a break statement.
class Solution(object):
    def searchRange(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]


class Solution(object):
    def searchRange(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
