## Area = length of shorter vertical line * distance between lines

## Start with the maximum width container and go to a shorter width container
## if there is a vertical line longer than the current container's shorter line.

class Solution:
    def maxArea(self, height):
        '''
        type height: List[int]
        rtype: int
        '''
        if len(height) == 0 or len(height) == 1:
            return 0
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
