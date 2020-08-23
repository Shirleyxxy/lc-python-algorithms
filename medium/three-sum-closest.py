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
