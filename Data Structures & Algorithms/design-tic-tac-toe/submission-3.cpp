class TicTacToe {
private:
    vector<int> rows;
    vector<int> cols;
    int size;
    int diagCount;
    int crossDiagCount;

public:
    TicTacToe(int n) {
        rows.assign(n, 0);
        cols.assign(n, 0);
        size = n;
        diagCount = 0;
        crossDiagCount = 0;
    }
    
    int move(int row, int col, int player) {
        int playerInd = (player == 1) ? 1 : -1;
        rows[row] += playerInd;
        cols[col] += playerInd;

        if (row == col) diagCount += playerInd;
        if (row == (size - col - 1)) crossDiagCount += playerInd;

        if (abs(rows[row]) == size || 
            abs(cols[col]) == size || 
            abs(diagCount) == size || 
            abs(crossDiagCount) == size) return player;
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
