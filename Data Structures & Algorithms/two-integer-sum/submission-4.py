class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for idx, num in enumerate(nums):
            if num not in idxs:
                idxs[num] = [idx]
            elif len(idxs[num]) == 1:
                idxs[num].append(idx)

        for idx, num in enumerate(nums):
            if (target - num) in idxs and idx!=idxs[target-num]:
                return [idxs[num][0], idxs[target-num][0]]
        return []
        