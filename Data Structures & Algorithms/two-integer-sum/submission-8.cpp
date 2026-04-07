class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> idxs;
        for (int i=0; i<nums.size(); i++) {
            const int diff = target - nums[i];
            if (idxs.find(diff)!=idxs.end()) return {idxs[diff], i};
            idxs.insert({nums[i], i}); 
        }
        return {};
    }
};
