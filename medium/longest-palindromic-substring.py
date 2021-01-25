## One of my favorite leetcode questions
## DP logical thinking: base cases + state transition
## Ref: http://gitlinux.net/2019-08-26-(5)-longest-palindromic-substring/

## Solution 1: Expand around center
## Time Complexity: O(N^2)
## Space Complexity: O(N)
class Solution:
    def longest_palindrome_at(self, s, l, r):
        '''
        Helper function to find the longest palindrom at indexes l, r.
        '''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        if not s: return ''
        res = ''
        for i in range(len(s)):
            str1 = self.longest_palindrome_at(s, i, i)
            str2 = self.longest_palindrome_at(s, i, i+1)
            longer = ''
            if len(str1) > len(str2):
                longer = str1
            else:
                longer = str2
            if len(longer) > len(res):
                res = longer
        return res


## Solution 2: Optimized version of solution 1 (Preferred solution 1)
## Expand around the center
## Using the key parameter in max function
## Time Complexity: O(N^2)
## Space Complexity: O(N)
class Solution:
    def longest_palindrome_at(self, s, l, r):
        '''
        Helper function to find the longest palindrom at indexes l, r.
        '''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        if not s: return ''
        res = ''
        for i in range(len(s)):
            ## case 1, like "aba"; case 2, like "abba"
            res = max(self.longest_palindrome_at(s, i, i), self.longest_palindrome_at(s, i, i+1), res, key = len)
        return res


## Solution 3: (Better) optimized version of solution 1
## Expand around the center
## Using the key parameter in max function
## Using start, end index to keep track --> constant space
## Time Complexity: O(N^2)
## Space Complexity: O(1)
class Solution:
    def get_max_len(self, s, l, r):
        '''
        Helper function to find the length of the longest palindrom at indexes l, r.
        '''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        if not s: return ''
        start, end = 0, 0
        for i in range(len(s)):
            cur_max = max(self.get_max_len(s, i, i), self.get_max_len(s, i, i+1))
            if cur_max > end - start:
                start = i - (cur_max-1) // 2
                end = start + cur_max
        return s[start : end]


## Solution 4: Bottom-up DP
## Time Complexity: O(N^2)
## Space Complexity: O(N^2)
## Note: the l and r indices are the exact indices for the substring
## In the previous solutions, the indices are for slicing
class Solution:
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        # 2D array
        dp = [[False] * len(s) for _ in range(len(s))]
        l, r = 0, 0
        # dynamic programming
        '''
          a b a
          0 1 2
      a 0 T X X
      b 1 F T X
      a 2 T F T
        '''
        for i in range(len(s)):
            # we only need the left bottom part of the 2D array
            start, end = i, i
            while start >= 0:
                # base case 1: start = end
                if start == end:
                    dp[start][end] = True
                # base case 2: start+1 = end, s[start] == s[end]
                elif start+1 == end and s[start] == s[end]:
                    dp[start][end] = True
                # state transition
                else:
                    dp[start][end] = dp[start+1][end-1] and (s[start] == s[end])
                # if dp[start][end] is palindromic, check if it is longer than the current best solution
                if dp[start][end] and (end-start+1) > (r-l+1):
                    l = start
                    r = end
                start -= 1
        return s[l:r+1]


## Updated: Bottom-up DP (Preferred solution 2)
## Time Complexity: O(N^2)
## Space Complexity: O(N^2)
class Solution:
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        start, end = 0, 0

        # base case
        for i in range(len(s)):
            dp[i][i] = True

        for left in range(len(s)-1, -1, -1):
            for right in range(left+1, len(s)):
                if s[left] == s[right]:
                    # be careful here: two cases
                    if right - left == 1 or dp[left+1][right-1]:
                        dp[left][right] = True
                        # update start & end if we find a longer substring
                        if right - left + 1 > end - start + 1:
                            start = left
                            end = right
        return s[start:end+1]
