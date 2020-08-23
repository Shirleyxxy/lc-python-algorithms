## Array has duplicates
## Time Complexity: O(logN) for the most of the time, O(N) in the worst case
## Space Complexity: O(1)

## An interesting fact about the minimum element is that it is the only element
## in the given array which is smaller than its previous element.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtype: int
        '''
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end - start) // 2
            # tricky part
            if nums[start] == nums[mid] == nums[end]:
                if nums[start] > nums[start+1]:
                    return nums[start+1]
                start += 1
                if nums[end-1] > nums[end]:
                    return nums[end]
                end -= 1
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
