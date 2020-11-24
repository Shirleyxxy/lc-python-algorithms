## N = number of candidates
## T = target value
## M = minimal value among the candidates

## Time Complexity: O(N^(T/M+1))
## The execution of the backtracking is unfolded as a DFS traversal in an n-ary tree.
## The total number of steps during the backtracking would be the number of nodes in the tree.
## At each node, it takes a constant time to process.
## So we can say that the time complexity is linear to the number of nodes of the execution tree.

## Loose upper bound on the number of nodes: N^(T/M)
## T/M is the maximal depth of the tree

## Space Complexity: O(T/M) for the recursive function call stack

## Solution 1
## Pass down the current index of the for loop
## So we can skip the used candidates
class Solution:
    def combinationSum(self, candidates, target):
        '''
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        '''
        res = []
        candidates.sort()

        def dfs(index, target, path):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                dfs(i, target-candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return res


## Solution 2
class Solution:
    def combinationSum(self, candidates, target):
        '''
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        '''
        res = []
        candidates.sort()

        def dfs(target, path):
            if target == 0:
                res.append(path)
                return

            for cand in candidates:
                # early termination
                if cand > target: break
                # to avoid duplicate combinations
                if path and cand < path[-1]:
                    continue
                dfs(target - cand, path + [cand])

        dfs(target, [])
        return res
