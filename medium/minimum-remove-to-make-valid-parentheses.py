## Solution 1 - stack + set 
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def minRemoveToMakeValid(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        opens, closes = [], []
        for i, ch in enumerate(s):
            if ch == '(':
                opens.append(i)
            elif ch == ')':
                if opens:
                    opens.pop()
                else:
                    closes.append(i)
        indexes_to_remove = set(opens + closes)
        return ''.join([s[i] for i in range(len(s)) if i not in indexes_to_remove])


## Time Complexity: O(N) - much faster
## Space Complexity: O(N)
class Solution:
    def minRemoveToMakeValid(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        open = 0
        s = list(s)

        for i, ch in enumerate(s):
            if ch == '(':
                open += 1
            elif ch == ')':
                if open > 0:
                    open -= 1
                # remove the extra ')'
                else:
                    s[i] = ''

        # iterate from right to left to remove the extra '('
        for i in range(len(s)-1, -1, -1):
            if not open: break
            if s[i] == '(':
                s[i] = ''
                open -= 1

        return ''.join(s)
