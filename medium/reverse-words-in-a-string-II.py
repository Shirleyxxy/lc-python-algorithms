## Built-in function
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def reverseWords(self, s):
        '''
        Modify s in-place. Do not return anything.
        s: List[str]
        '''
        rev_words = ''.join(s).split(' ')[::-1]
        s[:] = list(' '.join(rev_words))


## Two-pointer technique
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def reverseWords(self, s):
        '''
        Modify s in-place. Do not return anything.
        s: List[str]
        '''
        def reverse(ls, left, right):
            while left < right:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1; right -= 1

        # reverse the entire string
        reverse(s, 0, len(s)-1)

        # reverse each word
        i, left = 0, 0
        while i < len(s):
            if s[i] == ' ':
                reverse(s, left, i-1)
                left = i + 1
            # the string only consists of a single word, no space
            elif i == len(s)-1:
                reverse(s, left, i)
            i += 1
