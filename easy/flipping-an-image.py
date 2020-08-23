## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def flipAndInvertImage(self, A):
        '''
        :type A: List[List[int]]
        :rtype: List[List[int]]
        '''
        return [[1 ^ el for el in reversed(row)] for row in A]


## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def flipAndInvertImage(self, A):
        '''
        :type A: List[List[int]]
        :rtype: List[List[int]]
        '''
        for row in A:
            for i in range((len(row)+1) // 2):
                row[i], row[len(row)-i-1] = 1 ^ row[len(row)-i-1], 1 ^ row[i]
        return A
