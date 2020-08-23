## Non-ASCII delimiter
## Each string may contain any possible characters out of 256 valid ASCII characters.
## Use a non-ASCII character for delimiter.
## Time Complexity: O(N) for encode & decode
## Space Complexity: O(1) for encode to keep the output (one string)
## O(N) for decode (a list of strings)

class Codec:
    def encode(self, strs):
        '''
        Encodes a list of strings to a single string.
        :type strs: [str]
        :rtype: str
        '''
        if len(strs) == 0:
            return chr(257)
        return chr(256).join(strs)


    def decode(self, s):
        '''
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: [str]
        '''
        if s == chr(257):
            return []
        return s.split(chr(256))
