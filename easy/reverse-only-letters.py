## Solution 1 - Stack
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def reverseOnlyLetters(self, S):
        '''
        :type S: str
        :rtype: str
        '''
        stack = [ch for ch in S if ch.isalpha()]
        res = []
        for ch in S:
            if ch.isalpha():
                res.append(stack.pop())
            else:
                res.append(ch)
        return ''.join(res)



## Solution 2 - Two pointers
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def reverseOnlyLetters(self, S):
        '''
        :type S: str
        :rtype: str
        '''
        left, right = 0, len(S)-1
        S = list(S)
        while left < right:
            if not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        return ''.join(S)
