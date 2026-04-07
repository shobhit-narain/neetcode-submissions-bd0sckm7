class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> s1Count(26, 0);
        vector<int> s2Count(26, 0);
        int m = s1.length();
        int n = s2.length();
        if (m > n) return false;
        for (int i = 0; i < m; i++) {
            ++s1Count[s1[i] - 'a'];
            ++s2Count[s2[i] - 'a'];
        }

        if (s1Count == s2Count) return true;
        for (int i = m; i < n; i++) {
            if (s1Count == s2Count) return true;
            ++s2Count[s2[i] - 'a'];
            --s2Count[s2[i - m] - 'a'];
        }

        return s1Count == s2Count;
    }
};
