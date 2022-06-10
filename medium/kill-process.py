## time complexity: O(N)
## space complexity: O(N)


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = collections.defaultdict(list)
        for i, parent in enumerate(ppid):
            children[parent].append(pid[i])

        queue = collections.deque([kill])
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            queue.extend(children[curr])

        return res
