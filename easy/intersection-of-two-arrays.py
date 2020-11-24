## Python set operations
## Time Complexity: O(N + M)
## O(N) is used to convert nums1 into set
## O(M) is used to convert nums2 into set
## For the intersection operator, O(N + M) on average
## Space Complexity: O(N + M)

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


## Searching (Brute force)
## Time Complexity: O(N * M)
## Iterate through nums1 and check for each value if this value in nums2 or not
## Space Complexity: O(1) if we do not consider res; O(N + M) in the worst case if we consider res
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


## Dictionary
## Time Complexity: O(N + M)
## Space Complexity: O(N)
class Solution:
    def intersection(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        d, res = {}, []
        for num in nums1:
            d[num] = d.get(num, 0) + 1

        for el in nums2:
            if el in d and d[el] > 0:
                res.append(el)
                d[el] = 0 # de-duplication
        return res


## Sorting / Two pointers
## Time Complexity: O(NlogN + MlogM)
## Space Complexity: O(1) if we do not consider res; O(N + M) in the worst case if we consider res
class Solution:
    def intersection(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res
