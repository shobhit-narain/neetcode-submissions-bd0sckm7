from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flt_list = defaultdict(dict)
        for s, d, p in flights:
            flt_list[s][d] = p
        q = [(0, src, 0)]
        min_cost_stop = {}
        while q:
            cost, sa, stop = heappop(q)
            if sa == dst: return cost
            if stop == k: continue
            for da, p in flt_list[sa].items():
                stop += 1
                cost += p
                if da not in min_cost_stop:
                    min_cost_stop[da] = (cost, stop)
                else:
                    if cost < min_cost_stop[da][0] or stop < min_cost_stop[da][1]:
                        heappush(q, (cost, da, stop))
                        min_cost_stop[da] = (cost, stop)
        return -1