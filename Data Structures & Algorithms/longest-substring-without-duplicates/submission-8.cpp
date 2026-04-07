class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() <= 1) return s.length(); 
        unordered_set<char> subs;
        subs.insert(s[0]);
        int res = 1;
        int l = 0;
        for (int r = 1; r < s.length(); r++) {
            while (subs.contains(s[r])) {
                subs.erase(s[l++]);
            }
            subs.insert(s[r]);
            res = max(res ,(int)subs.size());
        }
        return res;
    }
};
