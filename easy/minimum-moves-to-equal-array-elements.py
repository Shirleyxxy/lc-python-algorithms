## Before any moves: sum, n, min_num

## After m moves: all the numbers are x
## sum + m * (n-1) = x * n
## x = min_num + m (since the min_num will be incremented every time)

## Calculation:
## sum + m * (n-1) = (min_num + m) * n
## sum - m = min_num * n
## m = sum - min_num * n


class Solution:
    def minMoves(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        return sum(nums) - min(nums) * len(nums)
