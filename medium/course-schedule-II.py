## Time Complexity: O(V + E)
## Space Complexity: O(V + E)

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

        ## sources contain courses w/o prerequisites
        sources = deque()
        for course in in_degrees:
            if in_degrees[course] == 0:
                sources.append(course)

        ## start from courses w/o prerequisites
        while sources:
            course = sources.popleft()
            sorted_order.append(course)
            for child in graph[course]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        ## terminate when we can no longer remove edges from the graph
        ## case 1 - the edges left in the graph form cycles
        ## case 2 - all the edges have been removed & we have the topological order of the graph
        ## (aka. completed all the courses in the topological order)
        if len(sorted_order) == numCourses:
            return sorted_order
        return []
