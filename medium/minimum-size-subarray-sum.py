## Given an array of n positive integers and a positive integer s, find the minimal
## length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def minSubArrayLen(self, s, nums):
        '''
        :type s: int
        :type nums: List[int]
        :rtype: int
        '''
        window_sum, min_len = 0, float('inf')
        window_start = 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            while window_sum >= s:
                min_len = min(min_len, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
        return min_len if min_len != float('inf') else 0
