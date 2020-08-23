## Time Complexity: O(2^N)
## Space Complexity: O(2^N)

class Solution:
    def subsets(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        subsets = [[]]
        for num in nums:
            subsets.extend([subset + [num] for subset in subsets])
        return subsets
