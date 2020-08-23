## Two Pointers:
## One to keep track of the current element in the original array
## Another one just for the unique elements

## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return 0
        next_unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[next_unique-1]:
                nums[next_unique] = nums[i]
                next_unique += 1
        return next_unique


class Solution:
    def removeDuplicates(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_

# test
nums1 = []
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [1,1,2,2,3,4,5,5,6]
soln = Solution()
soln.removeDuplicates(nums1)
soln.removeDuplicates(nums2)
soln.removeDuplicates(nums3)
