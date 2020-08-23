## nums: an array of positive integers

## Time Complexity: O(N)
## Space Complexity: O(1)


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        count, left, product = 0, 0, 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count
