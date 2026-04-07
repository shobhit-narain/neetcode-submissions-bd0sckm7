class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def inbounds(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

        def bfs(x, y):
            to_visit = deque([(x, y)])
            while to_visit:
                for _ in range(len(to_visit)):
                    _x, _y = to_visit.popleft()
                    grid[_x][_y] = "0"
                    for ox, oy in dirs:
                        nx, ny = _x + ox, _y + oy
                        if inbounds(nx, ny) and grid[nx][ny] == "1":
                            to_visit.append((nx, ny))
            return None

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    grid[i][j] = "0"
                    islands += 1
        return islands