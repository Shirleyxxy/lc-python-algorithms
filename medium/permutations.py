## Time Complexity: O(N * N!)
## Space Complexity: O(N * N!)

class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        result = []
        self.permute_recursive(0, [], nums, result)
        return result

    def permute_recursive(self, pos, curr, nums, result):
        if pos == len(nums):
            result.append(curr)
        else:
            for i in range(len(curr)+1):
                new = list(curr)
                new.insert(i, nums[pos])
                self.permute_recursive(pos+1, new, nums, result)
