# You may assume that nums1 has enough space to hold additional
# elements from nums2

# merge and sort
class Solution:
    def merge(self, nums1, m, nums2, n):
        '''
        Do not return anything, modify nums1 in-place instead.
        :type nums1: List[int]
        :type nums2: List[int]
        :type m: int
        :type n: int
        '''
        nums1[:] = sorted(nums1[:m] + nums2)

# two pointers / start from the beginning
class Solution:
    def merge(self, nums1, m, nums2, n):
        '''
        Do not return anything, modify nums1 in-place instead.
        :type nums1: List[int]
        :type nums2: List[int]
        :type m: int
        :type n: int
        '''
        nums1_copy = nums1[:m]
        nums1[:] = []

        # two pointers
        p1 = 0
        p2 = 0

        # compare elements from nums1_copy and nums2
        # add the smaller one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


# two pointers / start from the end
class Solution:
    def merge(self, nums1, m, nums2, n):
        '''
        Do not return anything, modify nums1 in-place instead.
        :type nums1: List[int]
        :type nums2: List[int]
        :type m: int
        :type n: int
        '''
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1

        # set pointers for nums1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        nums1[:p2+1] = nums2[:p2+1]
