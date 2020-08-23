## Time Complexity: O(N^2)
## Space Complexity: O(N^2)
## dp[i][j]: at stone i, whether or not the frog can make a jump of size j
## the max jump size the frog can make at stone i is i+1

class Solution:
    def canCross(self, stones):
        '''
        :type stones: List[int]
        :rtype: bool
        '''
        n = len(stones)
        dp = [[False] * (n+1) for _ in range(n)]
        # The first stone's position is always 0; the first jump must be 1 unit
        dp[0][1] = True

        for i in range(1, n):
            # look into all the previous stones
            for j in range(0, i):
                dist = stones[i] - stones[j]
                # skip; not possible to come from stone j
                if dist < 0 or dist > i+1 or not dp[j][dist]: continue
                # if the frog's last jump was k units, then its next jump must be
                # either k-1, k, or k+1 units
                dp[i][dist-1], dp[i][dist], dp[i][dist+1] = True, True, True
                # land on the last stone --> can cross the river 
                if i == n-1: return True
        return False
