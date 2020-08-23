## Time Complexity: O(NlogN)
## Space Complexity: O(N)

from heapq import *

class Solution:
    def leastInterval(self, tasks, n):
        '''
        :type tasks: List[str]
        :type n: int
        :rtype: int
        '''
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        max_heap = []
        for task, freq in task_freq.items():
            heappush(max_heap, (-freq, task))

        interval_cnt = 0
        while max_heap:
            # try to execute n+1 tasks
            cnt, waitlist = 0, []
            while cnt <= n:
                interval_cnt += 1
                if max_heap:
                    freq, task = heappop(max_heap)
                    if freq < -1:
                        waitlist.append((freq+1, task))

                if not max_heap and not waitlist:
                    break
                else:
                    cnt += 1
            for freq, task in waitlist:
                heappush(max_heap, (freq, task))
        return interval_cnt
