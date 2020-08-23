## Trick: store index rather than actual value in the stack to handle duplicates in the input
## Circular array: loop twice

## Time Complexity: O(n)
## Space Complexity: O(n)

class Solution:
    def nextGreaterElements(self, nums):
        '''
        type nums: List[int]
        rtype: List[int]
        '''
        n = len(nums)
        stack, res = [], [-1] * n
        for i in range(n * 2):
            while stack and nums[i%n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return res
