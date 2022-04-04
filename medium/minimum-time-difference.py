## lc539: Minimum Time Difference
## Topics: string, list, sorting

## Time complexity: O(NlogN)
## Convert each "HH:MM" timestamp to minutes: O(N)
## Sorting the list of minutes: O(NlogN)
## Calculate the difference for each pair of adjacent elements: O(N)
## Find the minimum difference: O(N)

## Space complexity: O(N)

## Note / edge cases:
## How to articulate the need to append "timePoints[0] + 24 * 60" to the sorted list?
## circular array
## timestamps within 12 hours vs timestamps exceeding 12 hours

## sorted()
## zip()


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted([int(tp[:2]) * 60 + int(tp[-2:]) for tp in timePoints])
        timePoints.append(timePoints[0] + 24 * 60)
        return min(b - a for a, b in zip(timePoints, timePoints[1:]))
