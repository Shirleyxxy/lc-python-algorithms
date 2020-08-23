## Stack
## Time Complexity: 0(N), where N is the string length
## Space Complexity: O(N - D), where D is the total length for all duplicates

class Solution:
    def removeDuplicates(self, S):
        '''
        :type S: str
        :rtype: str
        '''
        stack = []
        for char in S:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
