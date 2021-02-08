## Dynamic Programming
## Time Complexity: O(N)
## Space Complexity: O(1)

## Case 1 - Positive Number
## Keep on multiplying the accumulated result

## Case 2 - Zero
## Reset your combo chain

## Case 3 - Negative Number
## Flip the largest combo chain to a very small number
## If you encounter another negative number, your combo chain can be saved

class Solution:
    def maxProduct(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        if not nums: return 0
        # keep track of the accumulated product of positive numbers
        max_so_far = nums[0]
        # to handle negative numbers
        min_so_far = nums[0]
        res = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            res = max(max_so_far, res)

        return res
