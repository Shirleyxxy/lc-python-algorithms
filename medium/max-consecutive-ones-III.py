## Time Complexity: O(N) - N is the count of numbers in the input array
## Space Complexity: O(1)

class Solution:
    def longestOnes(self, A, K):
        '''
        :type A: List[int]
        :type K: int
        :rtype: int
        '''
        window_start, max_len, ones_cnt = 0, 0, 0
        for window_end in range(len(A)):
            if A[window_end] == 1: ones_cnt += 1
            if window_end - window_start + 1 - ones_cnt > K:
                if A[window_start] == 1: ones_cnt -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len
