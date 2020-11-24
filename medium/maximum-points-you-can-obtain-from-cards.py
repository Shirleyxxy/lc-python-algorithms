## Time: O(N)
## Space: O(1)
class Solution:
    def maxScore(self, cardPoints, k):
        '''
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        '''
        window_size = len(cardPoints) - k
        min_sum = window_sum = sum(cardPoints[:window_size])
        for i in range(window_size, len(cardPoints)):
            window_sum += cardPoints[i] - cardPoints[i-window_size]
            min_sum = min(min_sum, window_sum)
        return sum(cardPoints) - min_sum
