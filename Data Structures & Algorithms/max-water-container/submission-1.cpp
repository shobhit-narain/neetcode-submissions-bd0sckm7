class Solution {
public:
    int maxArea(vector<int>& heights) {
        int res = 0;
        int l = 0;
        int r = heights.size() - 1;
        while (l < r) {
            int size = min(heights[l], heights[r]) * (r-l);
            res = max(res, size);
            if (heights[l] > heights[r]) r -= 1;
            else l += 1; 
        }
        return res;
    }
};
