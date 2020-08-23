## Time Complexity: O(N * M * logK)
## If we assume that both arrays have at least K elements then the time complexity
## can be simplified to O(K^2 * logK) because we are not iterating more than K elements
## in both arrays.
## Space Complexity: O(K)

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        '''
        max_heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                heappush(max_heap, (-(nums1[i]+nums2[j]), i, j))
                if len(max_heap) > k:
                    heappop(max_heap)
        result = []
        for (val, i, j) in max_heap:
            result.append([nums1[i], nums2[j]])
        return result
