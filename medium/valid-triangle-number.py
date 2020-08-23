## Brute force (Time limit exceeded)
## Time Complexity: O(N^3)
## Space Complexity: O(1)
class Solution:
    def triangleNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        count += 1
        return count



## Linear scan
## Time Complexity: O(N^2)
## Space Complexity: O(logN) for sorting 
class Solution:
    def triangleNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        count = 0
        nums.sort()
        for i in range(2, len(nums)):
            start, end = 0, i-1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    count += end - start
                    end -= 1
                else:
                    start += 1
        return count
