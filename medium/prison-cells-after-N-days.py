## Given K number of cells, there could be at most 2^K possible states.
## If the number of steps is larger than all possible states (N > 2^K),
## we are guaranteed to repeat.

## The number of possible states is 2^6 = 64 since the first and last cells
## will always be 0.

## Time Complexity: at most we could have 2^K possible states. While we run the simulation
## with N steps, we might need to run min(N, 2^K) steps without fast-forwarding in the worst case.
## For each simulation step, it takes O(K) time to process and evolve the state of cells.
## The overall time complexity is O(K * min(N, 2^K))

## Space Complexity: O(K * 2^K). The max number of states in the seen dictionary would be
## 2^K and each state takes O(K) space.

class Solution:
    def prisonAfterNDays(self, cells, N):
        '''
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        '''
        def _nextDay(cells):
            # the first and last cells will always be 0
            next_day_cells = [0] * len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    next_day_cells[i] = 1
            return next_day_cells

        seen = {}
        while N > 0:
            state_key = tuple(cells)
            if state_key in seen:
                # fast-forward to the step of N mod (len(cycle))
                # we only need to do the fast-forward once, if there is any
                N %= seen[state_key] - N
            else:
                seen[state_key] = N

            # check if there is still some steps remained
            # with or without the fast-forwarding
            if N >= 1:
                N -= 1
                cells = _nextDay(cells)

        return cells
