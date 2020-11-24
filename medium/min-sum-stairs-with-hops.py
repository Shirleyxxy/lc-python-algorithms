## HackerRank Problem:
## You are climbing a staircase. Each step has a cost you pay to step on it.
## You can jump between 1 and k steps at a time. What's the minimum you have to
## pay to reach the last step?

## Note: the input is a list "steps" of length n >= 1 and the max hop k >= 1.
## You start before step 0 and you have to reach after the last step (step n-1).


def minSumStairsWithHops(steps, k):
    memo = {}
    # min cost to pay to get to the top from step i.
    def cost(i):
        if i >= len(steps): return 0
        if i in memo: return memo[i]

        memo[i] = steps[i] + cost(i+1)
        for hop in range(2, k+1):
            memo[i] = min(memo[i], steps[i] + cost(i+hop))
        return memo[i]
    return cost(0)
