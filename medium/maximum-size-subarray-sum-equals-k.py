## time complexity: O(N)
## space complexity: O(N)

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cum_sum, max_len = 0, 0
        d = {}

        for i, num in enumerate(nums):
            cum_sum += num
            if cum_sum not in d:
                d[cum_sum] = i

            if cum_sum == k:
                max_len = max(max_len, i + 1)
            elif cum_sum - k in d:
                max_len = max(max_len, i - d[cum_sum-k])

        return max_len
