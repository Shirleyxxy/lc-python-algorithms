## Time Complexity: O(NlogN)
## Space Complexity: O(N)

from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings):
        '''
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        '''
        # start events (L, -H)
        # R for the max heap later
        events = [(L, -H, R) for L, R, H in buildings]
        # end events (R, 0)
        events += list({(R, 0, 0) for _, R, _ in buildings})
        # sort the events in left --> right order, then sort by H from high to low (why we use -H here)
        # -H is also for the max heap later
        events.sort()
        # res: for key points, [x, height]
        # live: max heap, [-height, ending position]
        res, live = [[0, 0]], [(0, float('inf'))]
        for pos, neg_h, R in events:
            # if it is a start event, push onto the heap
            if neg_h:
                heappush(live, (neg_h, R))
            # pop buildings that are already ended
            while live[0][1] <= pos:
                heappop(live)
            # if previous key point height != current highest height, edit the result
            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])

        return res[1:]
