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
    void bfs(vector<vector<char>>& grid, int r, int c) {
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0 ,-1}, {-1, 0}};
        queue<pair<int, int>> q;
        q.push({r, c});
        while (!q.empty()) {
            auto [x, y] = q.front();
            grid[x][y] = '0';
            q.pop();
            for (auto& dir : dirs) {
                int _x = x + dir[0];
                int _y = y + dir[1];

                if (_x >= 0 && _x < grid.size() && _y>=0 && _y < grid[0].size() && grid[_x][_y] == '1') {
                    q.push({_x, _y});
                }
            }
        }
    }
};
