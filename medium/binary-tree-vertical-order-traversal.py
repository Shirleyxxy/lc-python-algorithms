## column-wise order - based on its relative offset to the root node of the tree
## row-wise order - based on its level (guaranteed by the BFS traversal)
## modified level order traversal


## solution 1 (modified level order traversal + sorting)
## time complexity: O(NlogN) - N is the number of nodes in the tree
## space complexity: O(N)


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        # sort the obtained dictionary by its keys
        return [cols[k] for k in sorted(cols.keys())]


## solution 2 (modified level order traversal)
## time complexity: O(N)
## space complexity: O(N)


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        min_col, max_col = 0, 0

        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
                min_col = min(min_col, col - 1)
            if node.right:
                queue.append((node.right, col + 1))
                max_col = max(max_col, col + 1)

        return [cols[i] for i in range(min_col, max_col + 1)]
