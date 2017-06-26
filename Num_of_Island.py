class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [ [False] * n for x in range(m) ] # m * n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and not visited[x][y]:
                    # self.dfs(grid, x, y)
                    self.bfs(grid, visited, x, y, m, n)
                    ans += 1
        return ans
###############recursive dfs########################
    def dfs(self, grid, row, col):
        if (row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] != 1):
            return
        grid[row][col] = "#"
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
###############iterative bfs########################
    def bfs(self, grid, visited, x, y, m, n):
        queue = [ (x, y) ]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in zip( [1, 0, -1, 0], [0, 1, 0, -1] ):
                row, col = front[0] + p[0], front[1] + p[1]
                if 0 <= row < m and 0 <= col < n:
                    if grid[row][col] == 1 and not visited[row][col]:
                        visited[row][col] = True
                        queue.append((row, col))
