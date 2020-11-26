## Time Complexity: O(N^2)
## Let the time complexity be T(N).
## At each step for the worst case, the string can be divided into
## 2 parts and we require only one part for further computation.
## In the worst case, T(N) = T(N-2) + O(N) = O(N) + O(N-2) + O(N-4) + ... + O(1)
## which is O(N^2).
## Space Complexity: O(N) extra space for the reversed substring

class Solution:
    def shortestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        if not s or len(s) == 1:
            return s
        matched = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == s[matched]:
                matched += 1

        return s[::-1][:len(s)-matched] + self.shortestPalindrome(s[:matched-len(s)]) + s[matched-len(s):]
