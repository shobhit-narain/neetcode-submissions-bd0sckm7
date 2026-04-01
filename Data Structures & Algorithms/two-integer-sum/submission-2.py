class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for idx, num in enumerate(nums):
            if num not in idxs:
                idxs[num] = [idx]
            elif len(idxs[num]) == 1:
                idxs[num].append(idx)
        for num in nums:
            if num * 2 == target and len(idxs[num]) > 1:
                return idxs[num]
            if target - num in idxs:
                return [idxs[num][0], idxs[target-num][0]]
        return []
        