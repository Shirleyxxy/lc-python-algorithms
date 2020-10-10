class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        '''
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        '''
        websites_by_user = collections.defaultdict(list)
        # user1: [w1, w2, w3, ...]; website sorted in ascending timestamp order
        for t, u, w in sorted(zip(timestamp, username, website)):
            websites_by_user[u].append(w)

        cnt = collections.Counter()
        for websites_list in websites_by_user.values():
            # generate valid 3-sequences
            seqs = set(itertools.combinations(websites_list, 3))
            for seq in seqs:
                cnt[seq] += 1
        # sort descending by value, then in lexicographic order
        return min(cnt, key = lambda seq: (-cnt[seq], seq))
