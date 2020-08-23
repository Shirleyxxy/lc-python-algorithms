# Assume that the array is non-empty and the majority element
# always exist in the array.

# my solution (using Python dictionary)
class Solution:
    def majorityElement(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num, freq in freq.items():
            if freq > math.floor(len(nums) / 2):
                return num

# a variation of using dictionary
class Solution:
    def majorityElement(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        items = list(freq.items())
        return max(items, key = lambda item: item[1])[0]


# brute force (leetcode solution)
# NOT RECOMMENDED: Time Limit Exceeded
# quadratic time complexity: O(n^2)
class Solution:
    def majorityElement(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

## NOTE: There are many other solutions for this problem, such as
## Boyer-Moore Voting Algorithm, Divide and Conquer, Sorting, etc.
## (see leetcode solutions for more details.)
