## Time Complexity: O(m + n)
## Space Complexity: O(m + n)  -- including the returned value

class Solution:
    def intervalIntersection(self, A, B):
        '''
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        '''
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            s = max(A[i][0], B[j][0])
            e = min(A[i][1], B[j][1])
            # add the intersection to the result list
            if s <= e:
                res.append([s, e])
            # only increment the index for the earlier interval
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res
