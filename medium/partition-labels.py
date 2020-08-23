## Greedy: for each letter encountered, process the last occurrence of that letter
## and extend the current partition.
## Time Complexity: O(N)
## Space Complexity: O(1) - last_seen has no more than 26 characters

class Solution:
    def partitionLabels(self, S):
        '''
        :type S: str
        :rtype: List[int]
        '''
        last_seen, res = {}, []
        for i, ch in enumerate(S):
            last_seen[ch] = i

        size, rightmost = 0, 0
        for i, ch in enumerate(S):
            rightmost = max(rightmost, last_seen[ch])
            size += 1
            if i == rightmost:
                res.append(size)
                # reset for the next partition
                size = 0
        return res



## Two pointers (similar idea)
## Time Complexity: O(N)
## Space Complexity: O(1) - last_seen has no more than 26 characters
class Solution:
    def partitionLabels(self, S):
        '''
        :type S: str
        :rtype: List[int]
        '''
        last_seen = {ch:i for i, ch in enumerate(S)}
        left, right = 0, 0

        res = []
        for i, ch in enumerate(S):
            right = max(right, last_seen[ch])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res
