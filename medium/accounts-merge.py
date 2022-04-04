## DFS, graph
## For every pair of emails in the same account, draw an edge between those emails.
## The problem is to enumerate the connected components of this graph.

## Step 1 - construct the graph
## Step 2 - perform DFS to find connected components

## N = number of accounts
## K = maximum length of an account


## Time complexity: O(NKlogNK)
## Space complexity: O(NK)

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # construct the graph
        graph = defaultdict(list)  # email --> accounts
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                graph[email].append(i)

        visited = [False] * len(accounts)
        res = []
        # dfs - recursive process to find all the emails for each connected component
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in graph[email]:
                    dfs(neighbor, emails)

        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
