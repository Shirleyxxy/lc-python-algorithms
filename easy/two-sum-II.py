## input array is sorted

## Your returned answers (both index1 and index2) are not zero-based.

## You may assume that each input would have exactly one solution
## and you may not use the same element twice.

## solution 1 - using dict
class Solution:
    def twoSum(self, numbers, target):
        '''
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        '''
        d = {}
        for i, num in enumerate(numbers):
            remaining = target - num
            if remaining in d:
                return[d[remaining]+1, i+1]
            else:
                d[num] = i

## solution 2 - iteratively using two pointers (two-pointer technique)
class Solution:
    def twoSum(self, numbers, target):
        '''
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        '''
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] == target - numbers[r]:
                return [l+1, r+1]
            elif numbers[l] < target - numbers[r]:
                l += 1
            else:
                r -= 1
