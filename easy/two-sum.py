# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Brute Force
# Time: O(N^2)
class Solution:
    def twoSum(self, nums, target):
        '''
        nums: List[int]
        target: int
        rtype: List[int]
        '''
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Hashmap / Dictionary
# Time: O(N) - One Pass
class Solution:
    def twoSum(self, nums, target):
        '''
        nums: List[int]
        target: int
        rtype: List[int]
        '''
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target-num], i]
            dict[num] = i
            
