class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 2) return 0;
        int l = 0;
        int r = height.size() - 1;
        int maxl = height[l];
        int maxr = height[r];
        int res = 0;
        while (l < r) {
            if (maxl < maxr) {
                l++;
                maxl = max(height[l], maxl);
                res += (maxl - height[l]);
            } else {
                r--;
                maxr = max(height[r], maxr);
                res += (maxr  -height[r]);
            }
        }
        return res;
    }
};
