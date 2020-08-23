## Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
## Similar idea: lc121, best time to buy and sell stock

## Time Complexity: O(n)
## Space Complexity: O(n)

class Solution:
    def findMaxLength(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        balance, d = 0, {0:0}
        max_len = 0
        # index starts from 1
        for idx, num in enumerate(nums, start=1):
            if num == 0:
                balance -= 1
            else:
                balance += 1
            if balance in d:
                max_len = max(max_len, idx - d[balance])
            # store (balance, idx) in the dictionary when it is first encountered
            else:
                d[balance] = idx
        return max_len
