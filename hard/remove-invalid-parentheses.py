## Ref: http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/
## Idea: The one thing all these valid expressions have in common is that
## they will all be of the same length as compared to the original expression
## ==> find the number of misplaced parentheses

## DFS + Pruning
## Time Complexity: O(2^N)
## Space Complexity: O(N)
class Solution:
    def removeInvalidParentheses(self, s):
        '''
        :type s: str
        :rtype: List[str]
        '''
        res = []
        self.visited = set([s])
        self.dfs(s, self.countInvalid(s), res)
        return res


    def countInvalid(self, s):
        '''
        Return the number of misplaced left and right parentheses in s.
        '''
        left = right = 0
        d = {'(':1, ')':-1}
        for ch in s:
            left += d.get(ch, 0)
            right += 1 if left < 0 else 0
            left = max(left, 0)
        return left + right


    def dfs(self, s, n, res):
        if n == 0:
            res.append(s)
            return

        for i in range(len(s)):
            if s[i] in ['(', ')']:
                new_s = s[:i] + s[i+1:]
                # discard the string if the number of misplaced parentheses does not decrease
                if new_s not in self.visited and self.countInvalid(new_s) < n:
                    self.visited.add(new_s)
                    self.dfs(new_s, self.countInvalid(new_s), res)


## BFS
## Idea: with the input string s, we generate all possible states by removing one ( or )
## check if they are valid
## If found valid ones on the current level, put them to the final result list and we are done
## Otherwise, carry on to the next level (remove one more parenthesis).

## Time Complexity: In BFS, we handle the states level by level.
## In the worst case, we need to handle all the levels. We can analyze the time complexity
## level by level and add them up to get the final complexity.
## First level: only 1 string s, O(N) to check if it is valid
## Second level: (N choose N-1) * O(N-1)
## Third level: (N-1 choose N-2) * O(N-2)
## ......
## T(N) = (N choose N) * N + (N choose N-1) * (N-1) + (N-1 choose N-2) * (N-2) + ... + (2 choose 1) * 1 = O(N * 2^N)
## Space Complexity: O(N)
class Solution:
    def removeInvalidParentheses(self, s):
        '''
        :type s: str
        :rtype: List[str]
        '''
        def isValid(s):
            balance = 0
            d = {'(':1, ')':-1}
            for ch in s:
                balance += d.get(ch, 0)
                if balance < 0:
                    return False
            return balance == 0

        visited = set([s])
        res = []
        queue = collections.deque([s])
        finished = False
        while queue:
            curr_s = queue.popleft()
            if isValid(curr_s):
                finished = True
                res.append(curr_s)
            ## This ensures once we've found a valid parentheses pattern
            ## we don't do any further BFS using items pending in the queue
            ## since any further BFS would only yield strings of smaller length
            ## However, the items already in queue need to be processed since
            ## there could be other solutions of the same length
            if finished:
                continue
            for i in range(len(curr_s)):
                if curr_s[i] in ['(', ')']:
                    new_s = curr_s[:i] + curr_s[i+1:]
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
        return res


## BFS + Pruning
class Solution:
    def removeInvalidParentheses(self, s):
        '''
        :type s: str
        :rtype: List[str]
        '''
        def countInvalid(s):
            left = right = 0
            d = {'(':1, ')':-1}
            for ch in s:
                left += d.get(ch, 0)
                right += 1 if left < 0 else 0
                left = max(left, 0)
            return left + right

        visited = set([s])
        res = []
        queue = collections.deque([s])
        finished = False

        while queue:
            curr_s = queue.popleft()
            mismatch = countInvalid(curr_s)
            if mismatch == 0:
                finished = True
                res.append(curr_s)

            if finished:
                continue

            for i in range(len(curr_s)):
                if curr_s[i] in ['(', ')']:
                    new_s = curr_s[:i] + curr_s[i+1:]
                    ## Pruning
                    if new_s not in visited and countInvalid(new_s) < mismatch:
                        visited.add(new_s)
                        queue.append(new_s)
        return res
