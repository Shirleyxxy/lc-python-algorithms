## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def breakPalindrome(self, palindrome):
        '''
        :type palindrome: str
        :rtype: str
        '''
        # impossible to perform the replacement
        if len(palindrome) == 1:
            return ''
        # check the first half of the palindrome
        # change the first non 'a' character to 'a'
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        # if the string has only 'a', change the last character to 'b'
        return palindrome[:-1] + 'b'
