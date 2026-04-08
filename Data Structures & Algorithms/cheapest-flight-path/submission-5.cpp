class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        using pii = pair<int, int>;
        unordered_map<int, vector<pii>> nei;
        for (auto& flight : flights) {
            nei[flight[0]].push_back({flight[1], flight[2]});
        }
        vector<vector<int>> dist(n+1, vector<int>(k+5, INT_MAX));
        // for (int i=0; i<n; i++) dist[i] = new vector<int>(k+1, INT_MAX);
        dist[src][0] = 0;
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> q;
        q.push({0, src, -1});

        while (!q.empty()) {
            auto [cost, sa, stops] = q.top();
            // cout << cost << "," << sa << "," << stops <<"\n";
            q.pop();
            if (sa == dst) return cost;
            if (stops == k || dist[sa][stops + 1] < cost) continue;
            stops++;
            for (auto& [da, cst] : nei[sa]) {
                // cout << da << ", " << cst <<"\n";
                int nc = cost + cst;
                // cout << nc << ", " << dist[da][stops] <<"\n";
                if (dist[da][stops] > nc) {
                    // cout << "here" <<"\n";
                    q.push({nc, da, stops});
                    dist[da][stops] = nc;
                }
            }
        }
        return -1;
    }
};
