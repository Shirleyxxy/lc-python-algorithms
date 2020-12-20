## defaultdict + heap
class Leaderboard:

    def __init__(self):
        self.players = collections.defaultdict(int)

    def addScore(self, playerId, score):
        '''
        :type playerId: int
        :type score: int
        :rtype: None
        '''
        self.players[playerId] += score

    def top(self, K):
        '''
        :type K: int
        :rtype: int
        ---
        Time: O(NlogK)
        '''
        return sum(heapq.nlargest(K, self.players.values()))

    def reset(self, playerId):
        '''
        :type playerId: int
        :rtype: None
        '''
        del self.players[playerId]



## Counter object
class Leaderboard(object):
    '''
    Space: O(N)
    Space is more optimized than the first solution.
    '''

    def __init__(self):
        '''
        Time: O(1)
        '''
        self.players = collections.Counter()

    def addScore(self, playerId, score):
        '''
        Time: O(1)
        '''
        self.players[playerId] += score

    def top(self, K):
        '''
        Time: O(NlogK)
        '''
        return sum(v for i, v in self.players.most_common(K))

    def reset(self, playerId):
        '''
        Time: O(1)
        '''
        self.players[playerId] = 0
