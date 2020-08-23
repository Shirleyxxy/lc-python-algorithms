## Dynamic programming
## Time Complexity: O(N)
## Space Complexity: O(N) - space for max_left, max_right
class Solution:
    def trap(self, height):
        '''
        :type height: List[int]
        :rtype: int
        '''
        if not height: return 0
        area, n = 0, len(height)
        # max_left: max height from the left end up to index i
        # max_right: max height from the right end up to index i
        max_left, max_right = [0] * n, [0] * n
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]

        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        for j in range(n-2, -1, -1):
            max_right[j] = max(max_right[j+1], height[j])

        for i in range(1, n-1):
            area += min(max_left[i], max_right[i]) - height[i]
        return area


## Two pointers
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def trap(self, height):
        '''
        :type height: List[int]
        :rtype: int
        '''
        max_left, max_right = 0, 0
        left, right = 0, len(height)-1
        area = 0

        while left < right:
            # for pointer left, if it knows a taller bar
            # exists on his right side and if max_left is taller
            # it can contain some water
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    area += max_left - height[left]
                left += 1
            # same for pointer right
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    area += max_right - height[right]
                right -= 1
        return area
