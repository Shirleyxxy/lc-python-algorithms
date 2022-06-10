## Two pointers (solution 1)
## time complexity: O(N)
## space complexity: O(1)


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        # first scan to find the max height index
        max_h_idx, max_h = 0, 0
        for i, h in enumerate(height):
            if h > max_h:
                max_h = h
                max_h_idx = i

        water = 0

        # scan from left up to max height index and find all the water units up to the max height
        left_max = height[0]
        for i in range(max_h_idx):
            if height[i] > left_max:
                left_max = height[i]
            else:
                water += left_max - height[i]

        # scan from right down to max height index and find all the water units down to the max height
        right_max = height[-1]
        for j in range(len(height) - 1, max_h_idx, -1):
            if height[j] > right_max:
                right_max = height[j]
            else:
                water += right_max - height[j]

        return water


## Two pointers (solution 2)
## time complexity: O(N)
## space complexity: O(1)


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left, max_right = 0, 0
        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            # for pointer left, if a taller bar
            # exists on its right side and if max_left is taller
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
