## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums):
        '''
        :type nums:List[int]
        :rtype: int
        '''
        val = 0
        for num in nums:
            val ^= num
        return val
