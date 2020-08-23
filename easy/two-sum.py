#Given an array of integers, return indices of the two numbers
#such that they add up to a specific target.
#You may assume that each input would have exactly one solution,
#and you may not use the same element twice.


# my solution (brute force)
# n^2

class Solution:
    def twoSum(self, nums, target):
        '''nums: List[int], target: int, rtype: List[int]'''
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


# optimal solution (hashing)
class Solution:
    def twoSum(self, nums, target):
        '''nums: List[int], target: int, rtype: List[int]'''
        hashing_dict = {}
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining not in hashing_dict:
                hashing_dict[num] = idx
            else:
                return [hashing_dict[remaining], idx]
