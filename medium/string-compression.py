## Time Complexity: O(N)
## Space Complexity: O(1)
## Note 1: the group lengths that are 10 or longer will be split into multiple characters in chars
## Note 2: we modify "chars" in-place and return the new length of the array. However, the variable "chars"
## does not necessarily represent the new array in the end. (See the example below.) But the length returned
## will always be correct.
class Solution:
    def compress(self, chars):
        '''
        :type chars: List[str]
        :rtype: int
        '''
        slow, fast = 0, 0
        while fast < len(chars):
            chars[slow] = chars[fast]
            length = 1
            while fast + 1 < len(chars) and chars[fast+1] == chars[fast]:
                fast += 1
                length += 1
            if length > 1:
                for ch in str(length):
                    chars[slow+1] = ch
                    slow += 1
            fast += 1
            slow += 1
        # in the end, the index of the slow pointer
        # will be the length of the new array that was written
        return slow


chars = ['b', 'b', 'a', 'a', 'c', 'c', 'c']
print(compress(chars))
# (6, ['b', '2', 'a', '2', 'c', '3', 'c'])
