## Time Complexity: O(N * N!)
## Space Complexity: O(N * N!)

class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        result = []
        self.permute_recursive(0, [], nums, result)
        return result

    def permute_recursive(self, pos, curr, nums, result):
        if pos == len(nums):
            result.append(curr)
        else:
            for i in range(len(curr)+1):
                new = list(curr)
                new.insert(i, nums[pos])
                self.permute_recursive(pos+1, new, nums, result)


## My solution (Backtracking framework)
class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        res = []
        self.backtracking([], nums, res)
        return res

    def backtracking(self, curr, nums, res):
        if len(curr) == len(nums):
            res.append(curr[:])
        for num in nums:
            if num not in curr:
                curr.append(num)
                self.backtracking(curr, nums, res)
                curr.pop()


## Nested functions (from Pathrise guide)
## Solution 1: New copy for each child
class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        res = []

        def backtracking(perm):
            if len(perm) == len(nums):
                res.append(perm)
            for num in nums:
                if num not in perm:
                    backtracking(perm + [num])

        backtracking([])
        return res


## Solution 2: Single state modified in-place
class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        res = []
        perm = []

        def backtracking():
            if len(perm) == len(nums):
                res.append(perm[:])
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtracking()
                    perm.pop()

        backtracking()
        return res


## Solution 3: Extra info in state
class Solution:
    def permute(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        res = []
        perm = []
        # keep track of the set of remaining elements
        unused = set(nums)

        def backtracking():
            if len(perm) == len(nums):
                res.append(perm[:])
            for num in list(unused):
                perm.append(num)
                unused.remove(num)
                backtracking()
                perm.pop()
                unused.add(num)

        backtracking()
        return res



## HackerRank Variation
def permutationShifts(w):
    res = []
    d = {}
    for i, ch in enumerate(w):
        d[ch] = i

    def backtracking(perm):
        if len(perm) == len(w):
            perm_shift = ''
            for i, ch in enumerate(perm):
                perm_shift += str(i - d[ch]) + ch
            res.append(perm_shift)
            return
        else:
            for ch in w:
                if ch not in perm:
                    backtracking(perm + ch)

    backtracking('')
    return sorted(res)
