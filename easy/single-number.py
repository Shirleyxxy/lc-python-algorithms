## You must implement a solution with a linear runtime complexity and use only
## constant extra space.

## Intuition
## XOR(^): bitwise operator (exclusive or)
## logical operation

## X | Y | X^Y
## 0 | 0 | 0
## 0 | 1 | 1
## 1 | 0 | 1
## 1 | 1 | 0

## We will always get the single element because all the same ones will evaluate to 0 and 0 ^ single_number = single_number.

## Time Complexity: O(N)
## Space Complexity: O(1)


class Solution:
    def singleNumber(self, nums):
        """
        :type nums:List[int]
        :rtype: int
        """
        val = 0
        for num in nums:
            val ^= num
        return val
