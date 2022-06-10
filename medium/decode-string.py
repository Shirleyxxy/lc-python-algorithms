## stack
## time complexity: O(N)
## space complexity: O(N)


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num, res = [], 0, ""
        for ch in s:
            if ch.isalpha():
                res += ch
            elif ch.isdigit():
                num = 10 * num + int(ch)
            elif ch == "[":
                stack.append((num, res))
                num, res = 0, ""  # reset
            else:
                n, prev = stack.pop()
                res = prev + n * res
        return res
