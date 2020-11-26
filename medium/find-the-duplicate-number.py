## Solution 1: Brute force O(N^2)

## Solution 2: Sorting
## Time Complexity: O(NlogN)
## Space Complexity: O(1) (no extra space since we modify the input array in place)
class Solution:
    def findDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


## Solution 3: Set
## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def findDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


## Solution 4: Cyclic sort
## We try to place each number on its correct index
## Since there is only one duplicate, if while swapping the number with its index
## both the numbers being swapped are the same, we have found our duplicate
## Time Complexity: O(N)
## Space Complexity: O(1) but modifies the input array
class Solution:
    def findDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[i] == nums[j] and i != j:
                return nums[i]
            else:
                i += 1


## Solution 5: Cycle detection (Slow & fast pointers)
## What if we want O(N) time, constant space, and we are not allowed to modify the input array?
## Time Complexity: O(N)
## Space Complexity: O(1) and we do not modify the input array
class Solution:
    def findDuplicate(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        ## find the intersection point
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        ## find the cycle entrance (the duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
