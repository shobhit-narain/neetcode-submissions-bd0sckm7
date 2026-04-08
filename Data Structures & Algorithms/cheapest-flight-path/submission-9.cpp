class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        using ti = tuple<int, int, int>;
        unordered_map<int, vector<pair<int, int>>> nei;
        for (auto& flight : flights) {
            nei[flight[0]].push_back({flight[1], flight[2]});
        }
        vector<vector<int>> dist(n+1, vector<int>(k+1, -1));
        dist[src][0] = 0;
        priority_queue<ti, vector<ti>, greater<ti>> q;
        q.push({0, src, -1});

        while (!q.empty()) {
            auto [cost, sa, stops] = q.top();
            q.pop();
            if (sa == dst) return cost;
            if (stops == k) continue;
            stops++;
            for (auto& [da, cst] : nei[sa]) {
                int nc = cost + cst;
                if (dist[da][stops] == -1 | dist[da][stops] > nc) {
                    q.push({nc, da, stops});
                    dist[da][stops] = nc;
                }
            }
        }
        return -1;
    }
};
