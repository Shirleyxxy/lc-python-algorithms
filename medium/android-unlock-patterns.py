## Time Complexity: O(N!)
## Space Complexity: O(N)
## N is maximum pattern length

class Solution:
    def numberOfPatterns(self, m, n):
        '''
        :type m: int
        :type n: int
        :rtype: int
        '''
        # from a number in the keypad we can reach any other number, but can't reach the ones
        # that have a number as an obstacle in between unless we have previously visited the "obstacle".
        self.skip = {(1,3):2, (3,1):2, (4,6):5, (6,4):5, (7,9):8, (9,7):8, (1,9):5, (9,1):5,
                     (3,7):5, (7,3):5, (1,7):4, (7,1):4, (2,8):5, (8,2):5, (3,9):6, (9,3):6}
        self.num_patterns = 0
        for num in range(1, 10):
            self.visited = set()
            self.dfs(num, 1, m, n)
        return self.num_patterns


    def dfs(self, num, count, m, n):
        # the valid patterns have length in [m, n]
        if m <= count <= n:
            self.num_patterns += 1
        # finish if we reach length count n
        if count == n:
            return

        self.visited.add(num)
        for next_num in range(1, 10):
            if next_num not in self.visited:
                # if starting from num, there is an obstacle to reach next_num and the obstacle
                # number has not been visited before, skip this path
                if (num, next_num) in self.skip and self.skip[(num, next_num)] not in self.visited:
                    continue
                self.dfs(next_num, count+1, m, n)
        # backtracking
        self.visited.remove(num)
