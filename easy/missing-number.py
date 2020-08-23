## Solution 1 - Cyclic sort
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        i = 0
        while i < len(nums):
            j = nums[i]
            if j < len(nums) and j != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)


## Solution 2 - Addition & subtraction (asked during an Apple interview)
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        n = len(nums)
        all = (0+n) * (n+1) // 2
        return all - sum(nums)


## Solution 3 - Bit manipulation
## Taking XOR of a number with itself returns 0
## So we XOR the value of the largest number (n) with all the indices from 0 to n-1
## and with all the values in our array
## Similar idea to cyclic sort in some way 
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
