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


## Backtracking framework
## Nested function + Modify in-place
## We construct the subsets by making a sequence of decisions. We start with
## an empty list and for each element in the set, we decide whether to include
## it in the subset or not.
class Solution:
    def subsets(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        subsets = []
        subset = []

        def backtracking(i):
            ## i is the index for the next item to make a decision
            if i == len(nums):
                subsets.append(subset[:])
            else:
                subset.append(nums[i])
                backtracking(i+1)
                subset.pop()
                backtracking(i+1)

        backtracking(0)
        return subsets
