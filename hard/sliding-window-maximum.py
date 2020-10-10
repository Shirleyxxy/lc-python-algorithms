## 1. Brute force (TLE)
## Time Complexity: O(N * K)
## Space Complexity: O(N - k + 1)
class Solution:
    def maxSlidingWindow(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        '''
        if not nums: return []
        if k == 0: return nums

        return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]


## 2. Deque
## Time Complexity: O(N) since each element is processed exactly twice
## its index added and then removed from the deque
## Space Complexity: O(N), since O(N - K + 1) is used for an output array
## and O(K) for a deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        '''
        # check edge cases
        if not nums: return []
        if k == 0: return []
        if k == 1: return nums

        # initialize deque
        dq = collections.deque()
        res = []
        for i in range(len(nums)):
            # Pop from the end indexes of smaller elements (they are useless)
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # Append the current index
            dq.append(i)
            # Pop from the head the index i-k if it's still in the dq since it falls out of
            # the window; the range is [i-k+1, i]
            if dq[0] == i - k:
                dq.popleft()
            # Append the current window max to the res if our window has reached size k
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
