from heapq import heappush, heappop

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x == 0 and y == 0: return 0
        def get_next_moves(_x: int, _y: int) -> List[(int, int)]:
            return [
                (_x+1, _y+2),
                (_x+1, _y-2),
                (_x+2, _y+1),
                (_x+2, _y-1),
                (_x-1, _y+2),
                (_x-1, _y-2),
                (_x-2, _y+1),
                (_x-2, _y-1),
            ]
        
        steps = 0
        curr = [(0, (0, 0))]
        visited = set([(0, 0)])

        while curr:
            dist, node = heappop(curr)
            if node == (x, y): return dist
            for n in get_next_moves(node[0], node[1]):
                if n not in visited and n[0] >= -2 and n[1] >= -2:
                    visited.add(n)
                    heappush(curr, (dist+1, n))
        return -1
