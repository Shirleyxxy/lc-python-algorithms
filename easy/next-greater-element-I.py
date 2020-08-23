## Monotonic Stack
## d: store the result for (element, next_greater_element)
## Iterate over nums2 from left to right. Push every element on the stack if it is
## less than the previous element on the top of the stack.
## If we encounter an element nums[i] such that nums[i] > stack[-1], we keep on popping
## all the elements from stack until we encounter stack[k] such that stack[k] <= nums[i].
## For every element popped out of the stack stack[j], we put the popped element and its
## next greater element into the dictionary d[stack[j]] = nums[i].

## Time Complexity: O(m + n)
## The entire nums2 array (of size n) is scanned only once.
## The nums1 array is also scanned only once.

## Space Complexity: O(m + n)
## stack and d of size n is used, and res array of size m is used.
## n = len(nums2), m = len(nums1)

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        '''
        type nums1: List[int]
        type nums2: List[int]
        rtype: List[int]
        '''
        stack, d = [], {}
        res = []
        for el in nums2:
            while len(stack) > 0 and stack[-1] < el:
                d[stack.pop()] = el
            stack.append(el)

        for el in nums1:
            # if not found, output -1
            res.append(d.get(el, -1))

        return res
