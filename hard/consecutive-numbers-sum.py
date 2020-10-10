## Idea:
## N can be expressed as sum of k, k+1, k+2, ..., k+(i-1), where k is a positive integer.
## N = k * i + (i-1)*i / 2  => k * i = N - (i-1)*i / 2
## Which implies that as long as N - (i-1)*i / 2 is k times of i, we get a solution corresponding to i.
## Hence, iteration of all possible values of i, starting from 1, will cover all cases of the problem.


## Time Complexity: O(sqrt(N)) since i ~ N ^ 0.5
## Space Complexity: O(1)
class Solution:
    def consecutiveNumbersSum(self, N):
        '''
        :type N: int
        :rtype: int
        '''
        i, cnt = 1, 0
        while N > (i-1)*i / 2:
            if (N - (i-1)*i / 2) % i == 0:
                cnt += 1
            i += 1
        return cnt
