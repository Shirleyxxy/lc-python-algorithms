## Greedy Algorithm
## Time Complexity: O(N*logN) because of sorting
## Space Complexity: O(1)

class Solution:
    def twoCitySchedCost(self, costs):
        '''
        :type costs: List[List[int]]
        :rtype: int
        '''
        # sort by the difference in the costs which the company has by sending a person
        # to city A and not to city B
        costs.sort(key = lambda c:c[0] - c[1])
        n = len(costs) // 2
        # to optimize the total costs
        # send the first N people to the city A and the others to the city B
        return sum(costs[i][0] for i in range(n)) + sum(costs[i][1] for i in range(n, 2*n))
