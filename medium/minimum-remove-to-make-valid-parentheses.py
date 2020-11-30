## Solution 1 - Stack + set
## Identify all indexes that should be removed
## Build a new string with removed indexes
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
        ## Using set is much faster
        ## Checking if an item is in a set is O(1)
        indexes_to_remove = set(opens + closes)
        return ''.join([s[i] for i in range(len(s)) if i not in indexes_to_remove])



## Solution 2 - Two iterations (left to right + right to left)
## Time Complexity: O(N)
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
