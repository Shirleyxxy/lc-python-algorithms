## defaultdict + heap
## time complexity:
## addScore: O(1)
## top: O(NlogK)
## reset: O(1)

## space complexity:
## O(N + K)
## O(N) for dictionary
## O(K) for heap


class Leaderboard:
    def __init__(self):
        self.players = collections.defaultdict(int)

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.players[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        min_heap = []
        for score in self.players.values():
            heappush(min_heap, score)
            if len(min_heap) > K:
                heappop(min_heap)
        return sum(min_heap)

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.players[playerId]
