## My solution
class Solution:
    def runningSum(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        if not nums: return []
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[-1] + nums[i])
        return res


## Some other Pythonic solutions
## Built-in function, very fast
from itertools import accumulate
class Solution:
    def runningSum(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        return list(accumulate(nums))


## Iterative
class Solution:
    def runningSum(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums


class Solution:
    def runningSum(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
