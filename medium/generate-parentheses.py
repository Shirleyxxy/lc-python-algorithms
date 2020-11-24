## Recursion
## Time Complexity: O(N * 2^N)
## Space Complexity: O(N * 2^N)
class Solution:
    def generateParenthesis(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        result = []
        self.generateParenthesisRec('', n, n, result)
        return result

    def generateParenthesisRec(self, curr, left_remain, right_remain, result):
        if left_remain == 0 and right_remain == 0:
            result.append(curr)
        else:
            if left_remain > 0:
                self.generateParenthesisRec(curr+'(', left_remain-1, right_remain, result)
            if right_remain > left_remain:
                self.generateParenthesisRec(curr+')', left_remain, right_remain-1, result)


## Queue
## Time Complexity: O(N * 2^N)
## Space Complexity: O(N * 2^N)
from collections import deque
class Solution:
    def generateParenthesis(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        result = []
        queue = deque()
        queue.append(['', 0, 0])
        while queue:
            curr, left_cnt, right_cnt = queue.popleft()
            if left_cnt == n and right_cnt == n:
                result.append(curr)
            else:
                # if we can add a left parentheses, add it
                if left_cnt < n:
                    queue.append([curr+'(', left_cnt+1, right_cnt])
                # if we can add a right parentheses, add it
                if right_cnt < left_cnt:
                    queue.append([curr+')', left_cnt, right_cnt+1])
        return result


## Backtracking framework
class Solution:
    def generateParenthesis(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        res = []

        def backtracking(curr, left_remain, right_remain):
            if right_remain < left_remain or left_remain < 0 or right_remain < 0:
                return
            if left_remain == 0 and right_remain == 0:
                res.append(curr)
                return
            backtracking(curr+'(', left_remain-1, right_remain)
            backtracking(curr+')', left_remain, right_remain-1)

        backtracking('', n, n)
        return res

## I like this solution better
## Modify "curr" in-place and only pass the counts into the recursive function
class Solution:
    def generateParenthesis(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        res = []
        curr = []

        def backtracking(left_cnt, right_cnt):
            if left_cnt > n or left_cnt < right_cnt:
                return
            if left_cnt == right_cnt == n:
                res.append(''.join(curr[:]))
            else:
                curr.append('(')
                backtracking(left_cnt+1, right_cnt)
                curr.pop()

                curr.append(')')
                backtracking(left_cnt, right_cnt+1)
                curr.pop()

        backtracking(0, 0)
        return res
