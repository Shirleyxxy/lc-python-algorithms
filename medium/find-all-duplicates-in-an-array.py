## Solution 1: Brute force O(N^2)
## Check for a second occurrence of every element in the rest of the array.


## Solution 2: Sorting
## Time Complexity: O(NlogN)
## Space Complexity: O(1) (no extra space since we modify the input array in place)
class Solution:
    def findDuplicates(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        duplicate_nums = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate_nums.append(nums[i])
        return duplicate_nums


## Solution 3: Set
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def findDuplicates(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        duplicate_nums = []
        seen = set()
        for num in nums:
            if num in seen:
                duplicate_nums.append(num)
            seen.add(num)
        return duplicate_nums


## Cyclic sort
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def findDuplicates(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        duplicate_nums = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicate_nums.append(nums[i])
        return duplicate_nums
