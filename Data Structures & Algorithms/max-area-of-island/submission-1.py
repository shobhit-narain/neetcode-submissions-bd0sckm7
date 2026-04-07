class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = 0

        def inbounds(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

        def bfs(x, y):
            to_visit = deque([(x, y)])
            area = 0
            while to_visit:
                for _ in range(len(to_visit)):
                    _x, _y = to_visit.popleft()
                    area += 1
                    grid[_x][_y] = 0
                    for ox, oy in dirs:
                        nx, ny = _x + ox, _y + oy
                        if inbounds(nx, ny) and grid[nx][ny] == 1:
                            to_visit.append((nx, ny))
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(bfs(i, j), res)
                    grid[i][j] = 0

        return res