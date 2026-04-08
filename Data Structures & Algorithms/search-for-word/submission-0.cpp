class Solution {
public:
    int N, M;

    bool exist(vector<vector<char>>& board, string word) {
        // unordered_map<string, char> nei;
        // for (int i = 0; i < word.size()-1; i++) {
        //     nei[word.substr(0, i)] = word[i+1];
        // }
        N = board.size();
        M = board[0].size();

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j<board[0].size(); j++) {
                if(dfs(board, word, 0, i, j)) return true;
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, string word, int idx, int x, int y) {
        if (idx == word.size()) return true;
        if (x < 0 || y < 0 || x >= N || y >=M || 
            board[x][y] != word[idx] || board[x][y] == '-1') {
                return false;
            }
        idx ++;
        board[x][y] = '-1';
        bool res = dfs(board, word, idx, x + 1, y) ||
                dfs(board, word, idx, x, y + 1) ||
                dfs(board, word, idx, x - 1, y) ||
                dfs(board, word, idx, x, y - 1);
        board[x][y] = word[idx];
        return res;
    }
};
