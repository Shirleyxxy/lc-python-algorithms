## Similar to lc340: longest substring with at most K distinct characters

## Time Complexity: O(N) - outer for loop + inner while loop, O(N + N) --> asymptotically O(N)
## Space Complexity: O(1) - the algorithm runs in constant space O(1) as there can be a maximum of
## three types of fruits stored in the frequency map.

class Solution:
    def totalFruit(self, tree):
        '''
        :type tree: List[int]
        :rtype: int
        '''
        max_num, window_start = 0, 0
        fruit_d = {}
        for window_end in range(len(tree)):
            fruit_d[tree[window_end]] = fruit_d.get(tree[window_end], 0) + 1
            while len(fruit_d) > 2:
                fruit_d[tree[window_start]] -= 1
                if fruit_d[tree[window_start]] == 0: del fruit_d[tree[window_start]]
                window_start += 1
            max_num = max(max_num, window_end - window_start + 1)
        return max_num
