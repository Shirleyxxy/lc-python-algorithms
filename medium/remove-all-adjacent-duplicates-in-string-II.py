## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def removeDuplicates(self, s, k):
        '''
        :type s: str
        :type k: int
        :rtype: str
        '''
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                # need to use list
                # tuple object does not support item assignment
                stack.append([ch, 1])
            # if the current character is the same as the one before
            else:
                # increment the count on the top of the stack
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        # build the result string using characters and counts in the stack
        return ''.join(ch * cnt for ch, cnt in stack)
