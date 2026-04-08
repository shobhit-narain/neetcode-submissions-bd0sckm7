class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;

        for (int i = 0; i < grid.size(); i ++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    bfs(grid, i, j);
                    res++;
                }
            }
        }
        return res;
    }

private:
    int dirs[4][2] = {{0, 1}, {1, 0}, {0 ,-1}, {-1, 0}};

    void bfs(vector<vector<char>>& grid, int r, int c) {
        if (r >= 0 && r < grid.size() && c>=0 && c < grid[0].size() && grid[r][c] == '1') return;
        queue<pair<int, int>> q;
        q.push({r, c});
        while (!q.empty()) {
            auto [x, y] = q.front();
            grid[x][y] = '0';
            q.pop();
            for (auto& dir : dirs) {
                q.push({x + dir[0], y + dir[1]});
            }
        }
    }
};
