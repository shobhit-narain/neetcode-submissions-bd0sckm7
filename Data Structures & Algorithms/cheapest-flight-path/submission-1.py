from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flt_list = defaultdict(dict)
        for s, d, p in flights:
            flt_list[s][d] = p
        q = [(0, src, -1)]
        min_cost_stop = defaultdict(dict)
        min_cost_stop[src][-1] = 0
        while q:
            cost, sa, stop = heappop(q)
            if sa == dst: return cost
            if stop == k: continue
            if not min_cost_stop[sa].get(stop) or min_cost_stop[sa][stop] > cost:
                min_cost_stop[sa][stop] = cost
            stop += 1
            for da, p in flt_list[sa].items():
                nc = cost + p
                if not min_cost_stop[da].get(stop) or min_cost_stop[da][stop] > nc:
                    min_cost_stop[da][stop] = nc
                    heappush(q, (nc, da, stop))
        return -1