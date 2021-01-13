## Time Complexity: O(N)
## Space Complexity: O(1) if we do not count the res list
class Solution:
    def summaryRanges(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[str]
        '''
        if not nums: return []
        res, i, left = [], 0, 0

        while i < len(nums)-1:
            if nums[i+1] > nums[i]+1:
                res.append(self.format(nums[left], nums[i]))
                left = i + 1
            i += 1
        res.append(self.format(nums[left], nums[i]))
        return res


    def format(self, left, right):
        if left == right:
            return str(left)
        else:
            return str(left) + '->' + str(right)



## Same idea in fewer lines
class Solution:
    def summaryRanges(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[str]
        '''
        res, left = [], 0
        format = lambda l, r: str(l) + '->' + str(r) if l != r else str(l)
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] - nums[i-1] > 1:
                res.append(format(nums[left], nums[i-1]))
                left = i
        return res
