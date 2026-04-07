class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        map<int, int> points;
        for (auto interval : intervals) {
            points[interval[0]]++;
            points[interval[1]]--;
        }

        vector<vector<int>> res;
        vector<int> curr;
        int act = 0;
        for (const auto& [k, v] : points) {
            if (curr.empty()) curr.push_back(k);
            act += v;
            if (act == 0) {
                curr.push_back(k);
                res.push_back(curr);
                curr.clear();
            }
        }
        return res;
    }
};
