## Python set operation
## Time Complexity: O(N + M)
## O(N) is used to convert nums1 into set
## O(M) is used to convert nums2 into set
## For the intersection operator, O(N + M) in the average case, O(N * M) in the worst case
## Space Complexity: O(N + M) in the worst case

class Solution:
    def intersection(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        return list(set(nums1) & set(nums2))


class Solution:
    def intersection(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        return list(set(nums1).intersection(set(nums2)))


## Searching
## Time Complexity: O(N * M)
## Iterate through nums1 and check for each value if this value in nums2 or not
## Space Complexity: O(N + M) in the worst case
class Solution:
    def intersection(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        res = []
        for num in nums1:
            if num not in res and num in nums2:
                res.append(num)
        return res
