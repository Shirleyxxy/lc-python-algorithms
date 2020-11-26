## BFS Topological Sorting
## Time Complexity: O(V + E)
## Space Complexity: O(V + E)

from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        '''
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        '''
        if numCourses <= 0: return False
        sorted_order = []

        in_degrees = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}

        ## build the graph
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
            ## remove edges
            for child in graph[course]:
                in_degrees[child] -= 1
                ## more courses w/o prerequisites will possibly appear
                if in_degrees[child] == 0:
                    sources.append(child)
        ## terminate when we can no longer remove edges from the graph
        ## case 1 - the edges left in the graph form cycles
        ## case 2 - all the edges have been removed & we have the topological order of the graph
        return len(sorted_order) == numCourses



## Same idea; simplifying the code
class Solution:
    def canFinish(self, numCourses, prerequisites):
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for child, parent in prerequisites:
            G[parent].append(child)
            degree[child] += 1
        sources = [course_i for course_i in range(numCourses) if degree[course_i] == 0]
        for course_i in sources:
            for child in G[course_i]:
                degree[child] -= 1
                if degree[child] == 0:
                    sources.append(child)
        return len(sources) == numCourses
