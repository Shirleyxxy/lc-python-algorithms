## Dictionary
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        cache = {}
        for num in nums:
            if num in cache:
                return True
            else:
                cache[num] = 1
        return False


## Set
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        return len(set(nums)) < len(nums)
