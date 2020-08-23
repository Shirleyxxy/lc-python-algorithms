## Stack
## Time Complexity: O(N)
## Space Complexity: O(N)


class Solution:
    def decodeString(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        stack, curr_num, curr_str = [], 0, ''
        for ch in s:
            if ch == '[':
                stack.append((curr_num, curr_str))
                # reset
                curr_num, curr_str = 0, ''
            elif ch == ']':
                num, prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            elif ch.isdigit():
                curr_num = 10 * curr_num + int(ch)
            else:
                curr_str += ch
        return curr_str
