# my solution

## The letters in J are guaranteed distinct
class Solution:
    def numJewelsInStones(self, J, S):
        '''
        :type J: str
        :type S: str
        :rtype: int
        '''
        num = 0
        J_set = set(J)
        for s in S:
            if s in J_set:
                num += 1
        return num

# leetcode (brute force)
class Solution:
    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)

# leetcode (hash set)
class Solution:
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)
