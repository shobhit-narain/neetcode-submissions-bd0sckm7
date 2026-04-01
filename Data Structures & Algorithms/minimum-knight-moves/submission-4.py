class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        results = {}

        def dfs(x, y):
            if (x, y) in results: return results[(x, y)]
            if x + y == 0:
                # base case: (0, 0)
                results[(x, y)] = 0
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                results[(x, y)] = 2
                return 2
            else:
                dist = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
                result[(x, y)] = dist
                return dist

        return dfs(abs(x), abs(y))