## Two Pointers
## Time Complexity: O(N^2 + NlogN) --> O(N^2)
## Space Complexity: O(N) for sorting (also depends on the implementation of the sorting algorithm)
class Solution:
    def threeSumClosest(self, nums, target):
        min_diff = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if target - curr_sum == 0: return target
                if abs(target - curr_sum) < abs(min_diff):
                    min_diff = target - curr_sum
                if target - curr_sum > 0: left += 1
                else: right -= 1
        return target - min_diff
