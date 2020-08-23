## Time Complexity: O(N*logN + N^3), asymptotically O(N^3)
## Space Complexity: O(N) for sorting 

class Solution:
    def threeSum(self, nums, target):
        triplets = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < target: left += 1
                elif curr_sum > target: right -= 1
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


    def fourSum(self, nums, target):
        quadruplets = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            triplets = self.threeSum(nums[i+1:], target-nums[i])
            for triplet in triplets:
                quadruplets.append([nums[i]] + triplet)
        return quadruplets
