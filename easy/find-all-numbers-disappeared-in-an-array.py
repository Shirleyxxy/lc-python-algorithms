## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        missing_nums = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing_nums.append(i + 1)
        return missing_nums
