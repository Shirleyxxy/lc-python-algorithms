## Solution 1: Compare the original string and its reverse.
## Time complexity: O(N)
## We need to iterate thrice through the string: filtering, reverse, and comparison.
## Space complexity: O(N), additional space needed to store the filtered string
class Solution:
    def isPalindrome(self, s):
        s = ''.join(el for el in s if el.isalnum()).lower()
        return s == s[::-1]



## Solution 2: Filtering + Two-pointer technique
## Time complexity: O(N), traverse over each character in the filtered string
## Space complexity: O(N), still used additional space to store the filtered string
class Solution:
    def isPalindrome(self, s):
        s = ''.join(el for el in s if el.isalnum()).lower()
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1; right -= 1
        return True



## Solution 3: Two-pointer technique
## Time complexity: O(N), traverse over each character at most once
## Space complexity: O(1), no additional space required at all
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1; right -= 1
        return True



#### Archived solutions (summer 2019)
class Solution:
    def isPalindrome(self, s):
        '''
        :type s: str
        :rtype: boolean
        '''
        s = s.strip().lower()
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = ''.join(s.split())
        #s = s.replace(' ', '')
        return s == s[::-1]

class Solution:
    def isPalindrome(self, s):
        '''
        :type s: str
        :rtype: boolean
        '''
        s = ''.join(re.findall(r'[\w]+', s)).lower()
        return s == s[::-1]
