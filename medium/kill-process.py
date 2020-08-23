## Time Complexity: O(N)
## Space Complexity: O(N)
class Solution:
    def killProcess(self, pid, ppid, kill):
        '''
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        '''
        result = [kill]
        # dictionary storing a particular process and the list of its direct children
        processes = collections.defaultdict(list)
        for i in range(len(ppid)):
            processes[ppid[i]].append(pid[i])
        # add the process to be killed to the return list
        j = 0
        while j < len(result):
            if result[j] in processes:
                result.extend(processes[result[j]])
            j += 1
        return result


## NOTE: Modifying the result list while looping through it is not always recommended.
## We can use queue for BFS.
## Time Complexity: O(N)
## Space Complexity: O(N)
from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid, ppid, kill):
        '''
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        '''
        # processes: dictionary storing a particular process and the list of its direct children
        processes, queue, res = defaultdict(list), deque([kill]), []
        for i in range(len(ppid)):
            processes[ppid[i]].append(pid[i])

        while queue:
            curr = queue.popleft()
            res.append(curr)
            queue.extend(processes[curr])
        return res
