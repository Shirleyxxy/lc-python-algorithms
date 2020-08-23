## Solution 1 - Stack

## Time Complexity: O(M+N)
## Space Complexity: O(M+N)

class Solution:
    def backspaceCompare(self, S, T):
        '''
        :type S: str
        :type T: str
        :rtype: boolean
        '''
        def build(str):
            res = []
            for ch in str:
                if ch != '#': res.append(ch)
                # make sure the stack is not empty
                elif res: res.pop()
            return ''.join(res)
        return build(S) == build(T)


## Solution 2 - Two pointers

## Time Complexity: O(M+N)
## Space Complexity: O(1)

class Solution:
    def backspaceCompare(self, S, T):
        '''
        :type S: str
        :type T: str
        :rtype: boolean
        '''
        def get_next_index(str, index):
            skip = 0
            while index >= 0:
                # find a backspace character
                if str[index] == '#': skip += 1
                # skip a non-backspace character
                elif skip > 0: skip -= 1
                # a valid character; terminate the loop
                else: break
                index -= 1
            return index

        idx_S = len(S) - 1
        idx_T = len(T) - 1

        while idx_S >= 0 or idx_T >= 0:
            s_next = get_next_index(S, idx_S)
            t_next = get_next_index(T, idx_T)
            # reached the end of both strings
            if s_next < 0 and t_next < 0: return True
            # reached the end of one of the strings
            if s_next < 0 or t_next < 0: return False
            # check if the characters are equal
            if S[s_next] != T[t_next]: return False

            idx_S = s_next - 1
            idx_T = t_next - 1

        return True


## itertools.zip_longest: it prints the values of iterables alternatively in sequence.
## If one of the iterables is printed fully, the remaining values are filled by the values
## assigned to fillvalue parameter.

class Solution:
    def backspaceCompare(self, S, T):
        '''
        :type S: str
        :type T: str
        :rtype: boolean
        '''
        def get_next_char(str):
            skip = 0
            for ch in reversed(str):
                if ch == '#': skip += 1
                elif skip > 0: skip -= 1
                else: yield ch
        return all(ch1 == ch2 for ch1, ch2 in itertools.zip_longest(get_next_char(S), get_next_char(T)))
