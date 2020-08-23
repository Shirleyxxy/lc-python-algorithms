## Time Complexity: O(N^2)
## Space Complexity: O(N) for sorting 

class Solution:
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < target:
                    count += right - left
                    left += 1
                else: right -= 1
        return count
