## time complexity: O(N)
## space complexity: O(N)

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = collections.Counter(s)
        steps = 0

        for ch in t:
            if freq[ch] > 0:
                freq[ch] -= 1
            else:
                steps += 1

        return steps
