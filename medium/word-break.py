## Solution 1 - Recursion with memoization
class Solution:
    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        '''
        def canBreak(s, m, wordDict):
            if s in m: return m[s]
            if s in wordDict:
                m[s] = True
                return True
            for i in range(1, len(s)):
                r = s[i:]
                if r in wordDict and canBreak(s[0:i], m, wordDict):
                    m[s] = True
                    return True
            m[s] = False
            return False
        return canBreak(s, {}, set(wordDict))


## Solution 2 - Dynamic Programming
## Time Complexity: O(n^2)
## Space Complexity: O(n)

# dp[i] = True means s[:i] can be segmented into a sequence of words in the wordDict
# len(dp) == n+1
# Base case: an empty string can be segmented into a sequence of empty strings

class Solution:
    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: boolean
        '''
        n = len(s)
        dp = [True] + [False] * n
        for i in range(n):
            for word in wordDict:
                if dp[i] and s[i:i+len(word)] == word:
                    dp[i+len(word)] = True
        return dp[-1]


## loop through index rather than word in the dictionary
class Solution:
    def wordBreak(self, s, wordDict):
        '''
        :type s: str
        :type wordDict: List[str]
        :rtype: boolean
        '''
        n = len(s)
        dp = [True] + [False] * n
        for i in range(n):
            for j in range(i, n):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]
