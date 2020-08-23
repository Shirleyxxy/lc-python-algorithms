## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def productExceptSelf(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        L, R, res = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        # L[i] would contain the product of all the numbers to the left of i
        # R[i] would contain the product of all the numbers to the right of i
        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = nums[i-1] * L[i-1]

        R[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            R[i] = nums[i+1] * R[i+1]

        for i in range(len(nums)):
            res[i] = L[i] * R[i]
        return res


## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def productExceptSelf(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        res = [0] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        R = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * R
            R *= nums[i]
        return res
