## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[int]
        '''
        # get the XOR of all the numbers
        # which is equal to num1 ^ num2
        # there must be a set bit (a bit with value 1)
        # in the XOR result since the two numbers are distinct
        all_num_XOR, num1, num2 = 0, 0, 0
        for num in nums:
            all_num_XOR ^= num
        # only 1 digit is equal to 1 in rightmost_set_bit
        rightmost_set_bit = 1
        while rightmost_set_bit & all_num_XOR == 0:
            rightmost_set_bit = rightmost_set_bit << 1
        # partition all the numbers into two groups
        for num in nums:
            # the bit is set
            if num & rightmost_set_bit != 0:
                num1 ^= num
            # the bit is not set
            else:
                num2 ^= num
        return [num1, num2]
