## Assumption: For each ID, there will be at least 5 scores.
## My solution
## Time: O(NlogN)
## Space: O(N)
from collections import defaultdict
class Solution:
    def highFive(self, items):
        '''
        :type items: List[List[int]]
        :rtype: List[List[int]]
        '''
        id2scores, res = defaultdict(list), []
        for item in items:
            id2scores[item[0]].append(item[1])

        for id in sorted(id2scores.keys()):
            top5_avg = sum(sorted(id2scores[id], reverse = True)[:5]) // 5
            res.append([id, top5_avg])

        return res


## Heap
## Time: O(NlogN)
## Space: O(N)
from collections import defaultdict
from heapq import *
class Solution:
    def highFive(self, items):
        '''
        :type items: List[List[int]]
        :rtype: List[List[int]]
        '''
        id2scores = defaultdict(list)
        for id, score in items:
            heappush(id2scores[id], score)
            if len(id2scores[id]) > 5:
                heappop(id2scores[id])
        res = [[i, sum(id2scores[i]) // 5] for i in sorted(id2scores)]
        return res
