from collections import defaultdict

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for start, end in intervals:
            d[start] += 1
            d[end] -= 1

        curr = []
        res = []
        active = 0
        for t in sorted(d.keys()):
            if not curr:
                curr = [t]
            active += d[t]
            if active == 0:
                curr.append(t)
                res.append(curr)
                curr = []

        return res