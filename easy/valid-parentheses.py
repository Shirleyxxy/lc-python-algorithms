## Time Complexity: O(n) as we simply traverse the given string one character at a time and
## push and pop operations on a stack take O(1) time.

## Space Complexity: O(n) as we push all opening brackets onto the stack and in the worst case
## we will end up pushing all the brackets onto the stack.

class Solution:
    def isValid(self, s):
        '''
        :type s: str
        :rtype: boolean
        '''
        stack = []
        dict = {'(':')', '{':'}', '[':']'}
        for el in s:
            if el in dict:
                stack.append(el)
            elif el in dict.values():
                if stack == [] or dict[stack.pop()] != el:
                    return False
            else:
                return False
        return stack == []
