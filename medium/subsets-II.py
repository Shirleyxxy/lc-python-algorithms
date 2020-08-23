## Time Complexity: O(2^N)
## Space Complexity: O(2^N)

class Solution:
    def subsetsWithDup(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        nums.sort()
        subsets = [[]]
        for i in range(len(nums)):
            # duplicate number
            if i > 0 and nums[i] == nums[i-1]:
                curr = [subset + [nums[i]] for subset in curr]
            else:
                curr = [subset + [nums[i]] for subset in subsets]
            subsets.extend(curr)
        return subsets
