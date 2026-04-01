class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for idx, num in enumerate(nums):
            idxs[num] = idx

        for idx, num in enumerate(nums):
            if (target - num) in idxs and idx!=idxs[target-num]:
                return [idx, idxs[target-num]]
        return []
        