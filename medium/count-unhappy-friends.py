## time complexity: O(N^2)
## space complexity: O(N)


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = {}
        for x, y in pairs:
            d[x] = set(preferences[x][:preferences[x].index(y)])
            d[y] = set(preferences[y][:preferences[y].index(x)])

        count = 0
        for i in d:
            for j in d[i]:
                if i in d[j]:
                    count += 1
                    break

        return count
