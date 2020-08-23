## Solution 1
## Time Complexity: O(N^2)
## Space Complexity: O(1)
## Clear logic yet time limit exceeded
class Solution:
    def subarraySum(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: int
        '''
        count = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, len(nums)):
                sum += nums[end]
                if sum == k: count += 1
        return count


## Can we optimize it by using some extra space?
## Solution 2
## Idea: Whenever the sum has increased by a value of k, we've found a subarray of sum = k.
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def subarraySum(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: int
        '''
        count = 0
        sum_freq, curr = {}, 0
        # account for the case when curr == k
        sum_freq[0] = 1
        for num in nums:
            curr += num
            if curr - k in sum_freq:
                count += sum_freq[curr - k]
            sum_freq[curr] = sum_freq.get(curr, 0) + 1
        return count
