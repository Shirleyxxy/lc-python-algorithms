## Time Complexity: O(V+E)
## Space Complexity: O(V+E)

from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        '''
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        '''
        sorted_order = []
        if numCourses <= 0: return sorted_order

        in_degrees = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}

        for prerequisite in prerequisites:
            child, parent = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            in_degrees[child] += 1

        sources = deque()
        for course in in_degrees:
            if in_degrees[course] == 0:
                sources.append(course)

        while sources:
            course = sources.popleft()
            sorted_order.append(course)
            for child in graph[course]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        if len(sorted_order) == numCourses:
            return sorted_order
        return []
