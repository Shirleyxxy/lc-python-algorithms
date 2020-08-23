# my solution (slicing)
class Solution:
    def reverseString(self, s):
        '''
        Do not return anything, modify s in-place instead.
        :type s: List[str]
        '''
        s[:] = s[::-1]

# in-place string function
class Solution:
    def reverseString(self, s):
        s.reverse()

# two pointer swap in a while loop (two-pointer technique)
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
