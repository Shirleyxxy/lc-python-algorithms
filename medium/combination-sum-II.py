## Time Complexity: O(2^N)
## Space Complexity: O(N)

class Solution:
    def combinationSum2(self, candidates, target):
        '''
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        '''
        res = []
        candidates.sort()

        def dfs(idx, target, path):
            ## Base case; found the solution
            if target == 0:
                res.append(path)
                return

            for i in range(idx, len(candidates)):
                ## no need to keep searching
                if candidates[i] > target:
                    break
                ## to avoid duplicate combinations
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i + 1, target - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return res
