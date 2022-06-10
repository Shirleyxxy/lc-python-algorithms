## reference: https://alexgolec.dev/google-interview-questions-deconstructed-the-knights-dialer/
## constraints: 1 <= n <= 5000

## solution 1: DFS / recursion (TLE)
## time complexity: 10 * 3^(N-1) calls --> exponential time O(3^N)
## space complexity: O(3^N)


class Solution:
    def knightDialer(self, n: int) -> int:
        init_positions = [(i, j) for i in range(3) for j in range(3)]
        init_positions.append((1, 3))

        res = 0
        for x, y in init_positions:
            res += self.move(x, y, n)
        return res % (10**9 + 7)


    def move(self, x, y, n):
        if n == 1:
            return 1

        directions = [(-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, 2), (2, 1), (1, -2), (2, -1)]

        count = 0

        for step_x, step_y in directions:
            new_x = x + step_x
            new_y = y + step_y
            # valid move
            if (0 <= new_x <= 2 and 0 <= new_y <= 2) or (new_x == 1 and new_y == 3):
                count += self.move(new_x, new_y, n-1)

        return count



## solution 2: dynamic programming
## time complexity: O(N)
## space complexity: O(1)

class Solution:
    def knightDialer(self, n: int) -> int:
        valid_moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        res = [1] * 10

        for i in range(n-1):  # O(N-1)
            next = [0] * 10
            for src in range(10):  # O(10)
                for dst in valid_moves[src]: # will run 3 times maximum
                    next[dst] += res[src]
            res = next

        return sum(res) % (10**9 + 7)
