## Make sure the "overlapping" area is valid.
## Time Complexity: O(1)
## Space Complexity: O(1)
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        '''
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        '''
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        bottom = max(rec1[1], rec2[1])
        up = min(rec1[3], rec2[3])
        if left < right and bottom < up:
            return True
        return False


## Rec2 must be either higher, lower, to the right, to the left of Rec1 if they do not overlap.
## Time Complexity: O(1)
## Space Complexity: O(1)
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        '''
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        '''
        if rec2[0] >= rec1[2] or rec2[1] >= rec1[3] or rec2[2] <= rec1[0] or rec2[3] <= rec1[1]:
            return False
        return True
