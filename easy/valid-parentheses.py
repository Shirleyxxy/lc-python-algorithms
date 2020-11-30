## Time Complexity: O(N) as we simply traverse the given string one character at a time and
## push and pop operations on a stack take O(1) time.

## Space Complexity: O(N) as we push all opening brackets onto the stack and in the worst case
## we will end up pushing all the brackets onto the stack.

class Solution:
    def isValid(self, s):
        '''
        :type s: str
        :rtype: boolean
        '''
        stack = []
        d = {'(':')', '{':'}', '[':']'}
        for el in s:
            if el in d:
                stack.append(el)
            elif el in d.values():
                if not stack or d[stack.pop()] != el:
                    return False
        return stack == []
