class TicTacToe:

    def __init__(self, n: int):
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = player
        if row == col:
            return player if all(self.grid[i][i] == player for i in range(self.n)) else 0
        return player if (
            all(self.grid[row][i] == player for i in range(self.n)) or \
            all(self.grid[j][col] == player for j in range(self.n))
            ) else 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
