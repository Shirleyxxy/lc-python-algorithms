## Time Complexity: O(N^2)
## Space Complexity: O(1)

class Solution:
    def findNextIndex(self, nums, is_forward, curr_index):
        '''
        :type nums: List[int]
        :type is_forward: bool
        :type curr_index: int
        :rtype: int
        '''
        direction = nums[curr_index] >= 0
        if direction != is_forward: return -1
        next_index = (curr_index + nums[curr_index]) % len(nums)
        if next_index == curr_index: return -1
        return next_index


    def circularArrayLoop(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        for i in range(len(nums)):
            is_forward = nums[i] >= 0
            slow, fast = i, i
            while True:
                slow = self.findNextIndex(nums, is_forward, slow)
                fast = self.findNextIndex(nums, is_forward, fast)
                if fast != -1:
                    fast = self.findNextIndex(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast: break
            if slow != -1 and slow == fast:
                return True
        return False


## Improve the time complexity to O(N) by keeping track of the numbers that have been evaluated for cycles.
## Time Complexity: O(N)
## Space Complexity: O(1) - no extra space, but the input array is modified

class Solution:
    def circularArrayLoop(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        if not nums or len(nums) < 2: return False
        for i, num in enumerate(nums):
            # use a distinct marker for each starting point
            mark = str(i)
            # keep exploring while the element has not been visited before, the direction does not change, and
            # there is no self loop
            while (type(nums[i]) == int) and (num * nums[i] > 0) and (nums[i] % len(nums) != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % len(nums)
            # a cycle is found
            if nums[i] == mark: return True
        return False
