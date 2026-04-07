class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> s1Count;
        unordered_map<char, int> s2Count;
        int m = s1.length();
        int n = s2.length();
        for (auto& s:s1) ++s1Count[s];
        for (int i = 0; i < m; i++)  ++s2Count[s2[i]];

        if (s1Count == s2Count) return true;

        for (int i = m; i < n; i++) {
            // cout << s2Count, s2[i], s2[i-m];
            if (s1Count == s2Count) return true;
            ++s2Count[s2[i]];
            --s2Count[s2[i - m]];
        }

        return s1Count == s2Count;
    }
};
