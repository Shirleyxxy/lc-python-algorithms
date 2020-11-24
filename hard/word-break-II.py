## DP with memoization
## s = word + postfix
## Time Complexity: O(N * 2^N)
## Space Complexity: O(N * 2^N)
class Solution:
    def wordBreak(self, s, wordDict):
        return self.break_rec(s, wordDict, {})

    def break_rec(self, s, wordDict, memo):
        if not s: return []
        if s in memo: return memo[s]

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(s) == len(word):
                res.append(word)
            else:
                res_postfix = self.break_rec(s[len(word):], wordDict, memo)
                for sub in res_postfix:
                    sub = word + ' ' + sub
                    res.append(sub)
        memo[s] = res
        return res
