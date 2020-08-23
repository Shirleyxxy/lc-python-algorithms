class Solution:
    def hammingDistance(self, x, y):
        '''
        Given two integers x and y, calculate the Hamming distance.
        The Hamming distance between two integers is the number of positions
        at which the corresponding bits are different.
        '''
        # use slice operation to remove the first two characters '0b'
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        max_len = max(len(x_bin), len(y_bin))

        # make both strings equal lengths by appending 0s on the left
        x_bin = x_bin.rjust(max_len, '0')
        y_bin = y_bin.rjust(max_len, '0')

        return sum(x != y for x, y in zip(x_bin, y_bin))
