## https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
## Time Complexity: O(log(min(M, N)))
## Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, A, B):
        '''
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        '''
        # make sure we always search the shorter array:
        # 1. the range becomes simpler [0, m]
        # 2. fewer values to examine
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        # input validation
        if n == 0:
            raise ValueError

        # A_min_cnt and A_max_cnt are the min and max number of values
        # A can contribute to the left half of A U B, respectively.
        # Since A is guaranteed to be the shorter array, we know it can
        # contribute to 0 or all of its values.
        A_min_cnt, A_max_cnt = 0, m
        # note the +1; make sure the median becomes the last element in this half
        left_half_len = (m + n + 1) // 2

        # binary search idea
        # search range is [0, m]
        # the length of the search range will be reduced by half after each loop
        while A_min_cnt <= A_max_cnt:
            # A_cnt is the number of values A will contribute to the left half of A U B
            A_cnt = A_min_cnt + (A_max_cnt - A_min_cnt) // 2
            # B_cnt is the number of values B will contribute to the left half of A U B
            B_cnt = left_half_len - A_cnt

            if A_cnt > 0 and A[A_cnt-1] > B[B_cnt]:
                # decrease A's contribution size
                A_max_cnt = A_cnt - 1
            elif A_cnt < m and B[B_cnt-1] > A[A_cnt]:
                # decrease B's contribution size (i.e increase A's contribution size)
                A_min_cnt = A_cnt + 1
            else:
                # neither x nor y lies beyond the left half of A U B.
                # we have found the right A_cnt.
                # guard against invalid index errors
                if A_cnt == 0: max_left = B[B_cnt-1]
                elif B_cnt == 0: max_left = A[A_cnt-1]
                else: max_left = max(A[A_cnt-1], B[B_cnt-1])
                # odd case
                if (m + n) % 2 == 1:
                    return max_left
                # guard against invalid index errors
                if A_cnt == m: min_right = B[B_cnt]
                elif B_cnt == n: min_right = A[A_cnt]
                else: min_right = min(A[A_cnt], B[B_cnt])
                # even case
                return (max_left + min_right) / 2.0
