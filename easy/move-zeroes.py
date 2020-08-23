class Solution:
    def moveZeroes(self, nums):
        '''
        type nums: List[int]
        rtype: None
        Modify nums in-place.
        '''
        nums_len = len(nums)
        last_nonzero_found_at = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[last_nonzero_found_at] = nums[i]
                last_nonzero_found_at += 1
        for i in range(last_nonzero_found_at, nums_len):
            nums[i] = 0
