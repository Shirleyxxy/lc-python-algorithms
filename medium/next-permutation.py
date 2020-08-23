## Time Complexity: O(N)
## Space Complexity: O(1)

## 1. Sequence in descending order --> no next larger permutation is possible --> reverse the sequence.
## 2. From the right, find the first pair of successive numbers such that nums[i-1] < nums[i].
## 3. Search for the smallest number in nums[i:] that is larger than nums[i-1] and swap it with nums[i-1].
## 4. After the swap, sort nums[i:] in ascending order to get the next larger permutation.

class Solution:
    def nextPermutation(self, nums):
        '''
        :type nums: List[int]
        :rtype: None
        Do not return anything, modify nums in-place instead. --> Swapping.
        '''
        # iterate from the right
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                # search for the smallest number in nums[i:] that is larger than nums[i-1]
                # nums[i:] in descending order
                j = i
                while j < len(nums) and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                # swap
                nums[i-1], nums[idx] = nums[idx], nums[i-1]
                # sort nums[i:] in ascending order to get the next permutation
                # nums[i:] currently in descending order
                nums[i:] = nums[i:][::-1]
                # break the loop since we only need to find the next permutation and modify the list
                # in-place from the first pair of successive numbers
                break
        # sequence in descending order, no next larger permutation is possible
        else:
            nums.reverse()
