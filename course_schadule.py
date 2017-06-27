class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        route = []
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, route):
                return []
        return route

    def dfs(self, graph, visited, node, route):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        for i in graph[node]:
            if not self.dfs(graph, visited, i, route):
                return False
        visited[node] = 1
        route.append(node)
        return True
