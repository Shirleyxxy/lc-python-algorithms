## Time Complexity:
## Sorting takes O(N*logN)
## We iterate through the nums once, and each time we iterate through
## the entire array using two pointers in a while loop --> O(N^2)

## O(N*logN + N^2), asymptotically O(N^2)

## Space Complexity: Ignoring the space required for the output array triplets,
## the space complexity will be O(N) which is required for sorting.

class Solution:
    def threeSum(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        triplets = []
        nums.sort()
        # the combinations for the last two elements have been considered
        for i in range(len(nums)-2):
            # sum of 3 positive numbers will always be greater than 0 --> terminate the loop
            if nums[i] > 0: break
            # skip the same target element to avoid duplicate triplets
            # repeating values are next to each other in a sorted array
            if i > 0 and nums[i] == nums[i-1]: continue
            # from here, it's a 2 sum problem
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                # find the triplet
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # skip the same element to avoid duplicate triplets
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # skip the same element to avoid duplicate triplets
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # move to the next **different** number
                    left += 1
                    right -= 1
        return triplets
