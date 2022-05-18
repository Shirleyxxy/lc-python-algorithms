## DFS, graph
## For every pair of emails in the same account, draw an edge between those emails.
## The problem is to explore the connected components of this graph.

## Step 1 - construct the graph
## Step 2 - perform DFS to explore each connected component

## N = number of accounts
## K = maximum length of an account


## Time complexity: O(NK * logNK)
## In the worst case, all the emails belong to a single person.
## The total number of emails will be N * K, and we need to sort
## these emails --> O(NK * logNK)

## DFS traversal will take NK operations as no email will be traversed more than once.

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


## Intuition:
## emails = nodes, an edge will signify that two emails are connected and hence belong to the same person.
## as long as two emails are connected by a path of edges, we know they belong to the same account.
## each connected component will represent one person, and the nodes in the connected component are the person's emails.
## ---> explore each connected component to find all the emails that belong to each person
## --> since a depth-first search is guaranteed to explore every node in a connected component
## we will perform a DFS on each connected component (person) to find all of the connected emails.
