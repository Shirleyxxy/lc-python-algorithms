class Solution:
    def rotate(self, nums, k):
        '''
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Do not return anything. Modify nums in-place instead.
        '''
        k, n = k % len(nums), len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]

class Solution:
    def rotate(self, nums, k):
        '''
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Do not return anything. Modify nums in-place instead.
        :type nums: List[int]
        :type k: int
        :rtype: None
        '''
        if k is None or k <= 0:
            return
        k, n = k % len(nums), len(nums)
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, left, right):
        '''
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: None
        '''
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -= 1

class Solution:
    def rotate(self, nums, k):
        '''
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Do not return anything. Modify nums in-place instead.
        '''
        for i in range(k):
            nums.insert(0, nums.pop())
