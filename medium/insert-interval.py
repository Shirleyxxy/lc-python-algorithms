## Time Complexity: O(N)
## Space Complexity: O(N)


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res, i = [], -1

        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)

            elif newInterval[1] < interval[0]:
                i -= 1
                break

            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        return res + [newInterval] + intervals[i + 1 :]
