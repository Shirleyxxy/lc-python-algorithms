class Solution:
    def compress(self, chars):
        '''
        Given an array of characters, compress it in-place.
        :type chars: List[str]
        :rtype: int
        '''
        anchor = write = 0
        for idx, char in enumerate(chars):
            # at the last character or when the next character is
            # different from the current character
            if idx + 1 == len(chars) or chars[idx + 1] != char:
                # group the characters
                chars[write] = chars[anchor]
                write += 1
                if idx > anchor:
                    # the length
                    for digit in str(idx - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = idx + 1
        # at the end, the position of the write head
        # will be the length of the answer that was written
        return write
