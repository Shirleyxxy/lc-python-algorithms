## Each element in the result should appear as many times as it shows
## in both arrays.
## The result can be in any order.

## Follow-up:
## 1. What if the given array is already sorted? How would you optimize?
## Use two pointers method, which will give us linear time and constant space complexity.

## 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
## Dictionary is a good choice as we can use a dictionary for the smaller array.

## 3. What if elements of nums2 are stored on disk, and the memory is
## limited such that you cannot load all elements into the memory at once?
## If nums1 fits into the memory, we can use dictionary to collect counts for nums1.
## Then we can sequentially load and process nums2.
## If neither of the arrays fit into the memory, we can apply some partial processing strategies:
## 1. Split the numeric range into subranges that fits into the memory.
## Collect counts only within a given subrange and call the method multiple times (for each subrange).
## 2. Use an external sort for both arrays. Load and process arrays sequentially.


## Dictionary / Counter
## Time: O(N + M)
## Space: O(min(N, M)) - we use dictionary to store numbers (and their counts) from the smaller array.
class Solution:
    def intersect(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        res = []
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        for num in nums2:
            if num in freq and freq[num] > 0:
                res.append(num)
                freq[num] -= 1
        return res


from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        counts = Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res


## Two Pointers
## Use this method if the input is sorted or when the output needs to be sorted
## Time: O(NlogN + MlogM)
class Solution:
    def intersect(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        '''
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
