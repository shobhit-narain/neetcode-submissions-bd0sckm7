class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int res = 0;
        for (int num : nums) {
            if (!numSet.contains(num - 1)) {
                int start = num;
                int curr = 1;
                while(numSet.contains(num+curr)) curr++;
                res = max(curr, res);
            }
        }
        return res;
    }
};
