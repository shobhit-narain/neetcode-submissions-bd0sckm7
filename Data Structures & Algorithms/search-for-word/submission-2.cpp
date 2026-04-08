class Solution {
public:
    int rows, cols;

    bool exist(vector<vector<char>>& board, string word) {
        rows = board.size();
        cols = board[0].size();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j<cols; j++) {
                if(dfs(board, word, 0, i, j)) return true;
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, string word, int idx, int x, int y) {
        if (idx == word.size()) return true;
        if (x < 0 || y < 0 || x >= rows || y >=cols || 
            board[x][y] != word[idx] || board[x][y] == '#') {
                return false;
            }
        board[x][y] = '#';
        bool res = dfs(board, word, idx+1, x + 1, y) ||
                dfs(board, word, idx+1, x, y + 1) ||
                dfs(board, word, idx+1, x - 1, y) ||
                dfs(board, word, idx+1, x, y - 1);
        board[x][y] = word[idx];
        return res;
    }
};
