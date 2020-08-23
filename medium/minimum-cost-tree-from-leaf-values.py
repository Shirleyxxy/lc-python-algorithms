## Solution 1 - Bottom-up DP
## dp[i,j]: smallest possible sum of the values of each non-leaf node from arr[i] to arr[j]
## Transition: split into left subtree and right subtree
## dp[i,j] = dp[i,k] + dp[k+1,j] + value of root
## The value of each non-leaf node is equal to the product of the largest leaf value
## in its left and right subtree respectively.
## value of root = max(arr[i:k+1]) * max(arr[k+1:j+1]), i <= k < j

## Time Complexity: O(n^3)
## Space Complexity: O(n^2)

class Solution:
    def mctFromLeafValues(self, arr):
        '''
        :type: List[int]
        :rtype: int
        '''
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        # base case
        for i in range(n):
            dp[i][i] = 0

        for len_ in range(2, n+1):
            for i in range(n-len_+1):
                j = i+len_-1
                # state transition
                for k in range(i, j):
                    root_val = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + root_val)

        return dp[0][n-1]


## Solution 2 - Greedy Algorithm
## 1. Find the leaf node with minimum value
## 2. Combine it with its smaller in-order neighbor to build a non-leaf node
## 3. Once we get the newly generated non-leaf node, the node with the minimum value is useless
## 4. Repeat it until there is only one node.

## Time Complexity: O(n^2)
class Solution:
    def mctFromLeafValues(self, arr):
        '''
        :type: List[int]
        :rtype: int
        '''
        res = 0
        while len(arr) > 1:
            min_idx = arr.index(min(arr))
            if 0 < min_idx < len(arr)-1:
                res += min(arr[min_idx-1], arr[min_idx+1]) * arr[min_idx]
            else:
                res += (arr[min_idx+1] if min_idx == 0 else arr[min_idx-1]) * arr[min_idx]
            arr.pop(min_idx)
        return res
