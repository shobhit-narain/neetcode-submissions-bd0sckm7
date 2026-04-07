class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> idxs;
        for (int i=0; i<nums.size(); i++) {
            if (idxs.contains(target-nums[i])) return {idxs[target-nums[i]], nums[i]};
            idxs[nums[i]] = i; 
        }
        return {};
    }
};
