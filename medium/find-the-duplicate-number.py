## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def findDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[i] == nums[j] and i != j:
                return nums[i]
            else:
                i += 1
