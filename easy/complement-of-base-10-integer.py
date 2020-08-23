## XOR of a number with its complement will result in a number that has all its bits set to 1.
## number ^ complement = all_bits_set
## number ^ number ^ complement = number ^ all_bits_set
## 0 ^ complement = number ^ all_bits_set
## complement = number ^ all_bits_set

## Time Complexity: O(b), where b is the number of bits required to store the given number
## Space Complexity: O(1)

class Solution:
    def bitwiseComplement(self, N):
        '''
        :type N: int
        :rtype: int
        '''
        if N == 0: return 1
        bit_count, n = 0, N
        while n > 0:
            bit_count += 1
            n = n >> 1
        all_bits_set = pow(2, bit_count) - 1
        return N ^ all_bits_set
