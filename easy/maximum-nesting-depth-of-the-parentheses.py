## time complexity: O(N)
## space complexity: O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, curr = 0, 0
        for ch in s:
            if ch == "(":
                curr += 1
                max_depth = max(max_depth, curr)
            if ch == ")":
                curr -= 1
        return max_depth
