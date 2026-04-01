
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem == '.':
                    continue
                if elem in rows[i]:
                    return False
                if elem in cols[j]:
                    return False
                if elem in boxs[i//3 * 3 + j//3]:
                    return False
                rows[i].add(elem)
                cols[j].add(elem)
                boxs[i//3 * 3 + j//3].add(elem)
        return True